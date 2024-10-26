from contracts import snek_token
from moccasin.boa_tools import VyperContract
from eth_utils import to_wei

INITIAL_SUPPLY = to_wei(1000, "ether")


def deploy_token() -> VyperContract:
    snek_contract = snek_token.deploy(INITIAL_SUPPLY)
    print(f"Deployed SnekToken at {snek_contract.address}")
    return snek_contract


def moccasin_main() -> VyperContract:
    return deploy_token()
