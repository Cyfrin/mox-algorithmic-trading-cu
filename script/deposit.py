import boa
from boa.contracts.abi.abi_contract import ABIContract
from moccasin.config import get_active_network
from script._setup_script import setup_script
from moccasin.boa_tools import VyperContract

REFERRAL_CODE = 0


def deposit_into_aave(
    pool_contract: ABIContract, token: VyperContract, amount: int
) -> int:
    allowed_amount = token.allowance(boa.env.eoa, pool_contract.address)
    if allowed_amount < amount:
        token.approve(pool_contract.address, amount)
    print(f"Depositing {token.name()} into Aave contract {pool_contract.address}")
    pool_contract.supply(token.address, amount, boa.env.eoa, REFERRAL_CODE)


def run_deposit_script(usdc, weth):
    active_network = get_active_network()
    aavev3_pool_address_provider = active_network.manifest_named(
        "aavev3_pool_address_provider"
    )
    pool_address: str = aavev3_pool_address_provider.getPool()
    pool_contract = active_network.manifest_named("pool", address=pool_address)
    # Deposit all USDC
    usdc_balance = usdc.balanceOf(boa.env.eoa)
    if usdc_balance > 0:
        deposit_into_aave(pool_contract, usdc, usdc_balance)
    # Deposit all WETH
    weth_balance = weth.balanceOf(boa.env.eoa)
    if weth_balance > 0:
        deposit_into_aave(pool_contract, weth, weth_balance)

    (
        totalCollateralBase,
        totalDebtBase,
        availableBorrowsBase,
        currentLiquidationThreshold,
        ltv,
        healthFactor,
    ) = pool_contract.getUserAccountData(boa.env.eoa)
    print(f"""User account data:
        totalCollateralBase: {totalCollateralBase}
        totalDebtBase: {totalDebtBase}
        availableBorrowsBase: {availableBorrowsBase}
        currentLiquidationThreshold: {currentLiquidationThreshold}
        ltv: {ltv}
        healthFactor: {healthFactor}
          """)


def moccasin_main():
    usdc, weth, _, _ = setup_script()
    run_deposit_script(usdc, weth)
