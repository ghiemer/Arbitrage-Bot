"""
RPC pool & fail-over – returns the currently fastest, healthy endpoint
"""
from __future__ import annotations
import asyncio, random, time
from typing import Dict, List
from web3 import AsyncWeb3, AsyncHTTPProvider
import yaml, os

with open("config/chains.yaml", "r") as f:
    CHAINS: Dict = yaml.safe_load(f)

_RPC_STATE: Dict[str, Dict] = {}   # {url: {"lat": float, "alive": bool}}

async def _ping(url: str) -> float | None:
    """Measure latency via eth_blockNumber."""
    try:
        w3 = AsyncWeb3(AsyncHTTPProvider(url, request_kwargs={"timeout": 3}))
        t0 = time.time()
        await w3.eth.block_number  # simple call
        return time.time() - t0
    except Exception:
        return None

async def _refresh_chain(chain: str):
    tasks = [_ping(url) for url in CHAINS[chain]["rpc"]]
    for url, latency in zip(CHAINS[chain]["rpc"], await asyncio.gather(*tasks)):
        _RPC_STATE[url] = {"lat": latency or 9e9, "alive": latency is not None}

def get_rpc(chain: str) -> str:
    """Returns the fastest active RPC; triggers refresh if needed."""
    if not _RPC_STATE:
        asyncio.run(_refresh_chain(chain))
    healthy = {u: d for u, d in _RPC_STATE.items() if d["alive"]}
    if not healthy:
        raise RuntimeError(f"No healthy RPC for {chain}")
    return min(healthy, key=lambda u: healthy[u]["lat"])

__all__ = ["get_rpc", "CHAINS"]
