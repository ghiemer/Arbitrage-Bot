"""
Creates & sends transactions; stub for dry-run only
"""
import os, logging
from web3 import Web3, HTTPProvider
from provider import get_rpc

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
MODE = os.getenv("MODE", "dryrun")
log = logging.getLogger(__name__)

def _sign_and_send(chain: str, tx: dict) -> str:
    if MODE == "dryrun":
        log.info("DRY-RUN tx: %s", tx)
        return "0xDRYRUN"
    w3 = Web3(HTTPProvider(get_rpc(chain)))
    signed = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    return w3.eth.send_raw_transaction(signed.rawTransaction).hex()

async def execute_trade(opportunity: dict) -> str:
    tx = {}  # TODO: build atomic swap route
    return _sign_and_send(opportunity["chain"], tx)
