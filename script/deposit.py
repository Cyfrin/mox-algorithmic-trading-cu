import boa
from boa.contracts.abi.abi_contract import ABIContractFactory
import json

REFERRAL_CODE = 0


def get_pool(aavev3_pool_address_provider):
    pool_address = aavev3_pool_address_provider.getPool()
    with open("abis/aave_pool.json", encoding="utf-8") as f:
        pool_abi = json.load(f)
        return ABIContractFactory("aave_pool", pool_abi).at(pool_address)


def deposit_into_aave(pool, token, amount):
    allowed_amount = token.allowance(boa.env.eoa, pool.address)
    if allowed_amount < amount:
        token.approve(pool.address, amount)

    pool.supply(token, amount, boa.env.eoa, REFERRAL_CODE)
