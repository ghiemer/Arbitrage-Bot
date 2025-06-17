"""
Einstiegspunkt: startet Price-Loop und verarbeitet Opportunities
"""
import asyncio, logging, os
from dotenv import load_dotenv
load_dotenv()

from scheduler import JobScheduler
from price_scanner import PriceScanner
from spread_analyzer import is_profitable
from gas_manager import gas_usd
from profit_calc import net_profit_usd
from swap_simulator import simulate_swap
from swap_executor import execute_trade
from logger import save_trade
from notifier import send_alert

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

MODE = os.getenv("MODE", "dryrun")
MIN_PROFIT = float(os.getenv("MIN_PROFIT_USD", "5"))

print("DEBUG DEX_API (main.py):", os.getenv("DEXSCREENER_API"))

async def process_tick(tick):
    buy_price = tick["price"]          # pretend same dex both sides for demo
    sell_price = buy_price * 1.01      # <-- TODO real second-dex price
    if not is_profitable(tick["pair"], buy_price, sell_price):
        return
    gas = await gas_usd(tick["pair"]["chains"][0])
    profit = net_profit_usd(buy_price, sell_price, amount=100, gas=gas, fee_pct=0.3)
    if profit < MIN_PROFIT:
        return
    ok = await simulate_swap(tick["pair"]["chains"][0], args={})
    if not ok:
        return
    tx = await execute_trade({"chain": tick["pair"]["chains"][0], "pair": tick["pair"]})
    save_trade({"chain": tick["pair"]["chains"][0], "pair": tick["pair"]}, tx, profit)
    await send_alert("✅", f"{tick['pair']['symbol']} profit {profit:.2f} USD | {tx}")

async def run_bot():
    scanner = PriceScanner()
    async for tick in scanner.stream_prices():
        asyncio.create_task(process_tick(tick))

if __name__ == "__main__":
    sched = JobScheduler()
    sched.add_job(run_bot, 0)          # non-stop price loop
    asyncio.run(sched.run_forever())
