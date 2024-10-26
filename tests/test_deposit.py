from eth.constants import ZERO_ADDRESS
from script.deposit import deposit_into_aave
from eth_utils import to_wei


def test_get_pool(pool):
    assert pool.address != "0x" + ZERO_ADDRESS.hex()


def test_deposit(pool, weth, account):
    amount = to_wei(1, "ether")
    if weth.balanceOf(account) < amount:
        weth.mint(account, amount)
    deposit_into_aave(pool, weth, amount)
