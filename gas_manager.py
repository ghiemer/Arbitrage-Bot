import asyncio, random
from provider import get_rpc
from web3 import AsyncWeb3, AsyncHTTPProvider

async def estimate_gas(chain: str) -> float:
    w3 = AsyncWeb3(AsyncHTTPProvider(get_rpc(chain)))
    base_fee = await w3.eth.gas_price
    # naive conversion – improve with oracle
    return base_fee / 1e18 * 210_000  # USD value later via price-feed

# simple cache
_GAS_CACHE = {}
async def gas_usd(chain: str) -> float:
    if chain not in _GAS_CACHE or random.random() < .1:
        _GAS_CACHE[chain] = await estimate_gas(chain)
    return _GAS_CACHE[chain]
