"""
1inch dry-run simulation (quick check) – placeholder for Tenderly
"""
import aiohttp, os

ONEINCH_API = os.getenv("ONEINCH_API")

async def simulate_swap(chain: str, args: dict) -> bool:
    url = f"{ONEINCH_API}/{chain}/swap"  # dryRun param?
    params = args | {"dryRun": "true"}
    async with aiohttp.ClientSession() as s:
        async with s.get(url, params=params, timeout=5) as r:
            return r.status == 200
