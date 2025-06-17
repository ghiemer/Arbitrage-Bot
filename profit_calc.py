def net_profit_usd(buy: float, sell: float, amount: float,
                   gas: float, fee_pct: float) -> float:
    gross = (sell - buy) * amount
    dex_fee = sell * amount * fee_pct / 100
    return gross - dex_fee - gas
