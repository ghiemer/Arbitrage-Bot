"""
Calculates spread & decides if a trade is worthwhile
"""
def calc_spread(buy_price: float, sell_price: float) -> float:
    return (sell_price - buy_price) / buy_price * 100

def is_profitable(pair_cfg: dict, buy_price: float, sell_price: float) -> bool:
    spread = calc_spread(buy_price, sell_price)
    return spread >= pair_cfg["min_spread_pct"]
