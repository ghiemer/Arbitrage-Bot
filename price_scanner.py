"""
Fetches DEX prices (DexScreener REST + later WS); provides async generator of ticks
"""
from __future__ import annotations
import aiohttp, asyncio, logging, os, yaml
from typing import AsyncGenerator, Dict, List

DEX_API = os.getenv("DEXSCREENER_API", "https://api.dexscreener.io/latest/dex/pairs")
with open("config/pairs.yaml") as f:
    PAIRS: List[Dict] = yaml.safe_load(f)

log = logging.getLogger(__name__)

class PriceScanner:
    def __init__(self):
        self.session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(5))

    async def _fetch_pair(self, pair: Dict) -> Dict | None:
        """REST fallback – DexScreener pair price."""
        symbols = pair["symbol"].replace("/", "")
        url = f"{DEX_API}/{symbols}?chain={pair['chains'][0]}"
        try:
            async with self.session.get(url) as r:
                js = await r.json()
                return {"pair": pair, "price": float(js["priceUsd"])}
        except Exception as e:
            log.warning("price fetch failed: %s", e)
            return None

    async def stream_prices(self) -> AsyncGenerator[Dict, None]:
        """Yield price dicts {pair, price} in round-robin fashion."""
        while True:
            tasks = [self._fetch_pair(p) for p in PAIRS]
            for res in filter(None, await asyncio.gather(*tasks)):
                yield res
            await asyncio.sleep(1)  # 1 second round
