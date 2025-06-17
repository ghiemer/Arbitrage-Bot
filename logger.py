import csv, logging, pathlib, datetime as dt

log = logging.getLogger(__name__)
_CSV = pathlib.Path("trades.csv")
if not _CSV.exists():
    _CSV.write_text("time,chain,pair,profit_usd,tx\n")

def save_trade(op, tx_hash: str, profit: float):
    with _CSV.open("a") as f:
        csv.writer(f).writerow([
            dt.datetime.utcnow().isoformat(),
            op["chain"], op["pair"]["symbol"], f"{profit:.4f}", tx_hash
        ])
