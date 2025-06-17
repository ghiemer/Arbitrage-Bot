from collections import defaultdict, deque
import time

_BLACKLIST = defaultdict(deque)  # pair -> deque[timestamps]

def record_revert(pair_key: str):
    _BLACKLIST[pair_key].append(time.time())

def is_blacklisted(pair_key: str, window: int = 600, max_reverts: int = 2) -> bool:
    # remove old entries
    dq = _BLACKLIST[pair_key]
    while dq and time.time() - dq[0] > window:
        dq.popleft()
    return len(dq) >= max_reverts
