import boa
from moccasin.config import get_active_network
from boa.contracts.abi.abi_contract import ABIContract
from typing import Tuple

STARTING_ETH_BALANCE = int(1000e18)
STARTING_USDC_BALANCE = int(100e6)
STARTING_WETH_BALANCE = int(1e18)


def _add_eth_balance():
    boa.env.set_balance(boa.env.eoa, STARTING_ETH_BALANCE)


def _add_token_balance(usdc: ABIContract, weth: ABIContract):
    master_minter = usdc.masterMinter()
    my_address = boa.env.eoa
    with boa.env.prank(master_minter):
        usdc.configureMinter(my_address, STARTING_USDC_BALANCE)
    usdc.mint(my_address, STARTING_USDC_BALANCE)
    weth.deposit(value=STARTING_WETH_BALANCE)


def setup_script() -> Tuple[ABIContract, ABIContract, ABIContract, ABIContract]:
    active_network = get_active_network()

    print("Starting setup script...")
    usdc = active_network.manifest_named("usdc")
    weth = active_network.manifest_named("weth")
    aave_protocol_data_provider = active_network.manifest_named(
        "aave_protocol_data_provider"
    )

    if active_network.is_local_or_forked_network():
        _add_eth_balance()
        _add_token_balance(usdc, weth)

    print("Getting atokens, this may take a while...")
    a_tokens = aave_protocol_data_provider.getAllATokens()
    a_usdc = None
    a_weth = None

    for a_token in a_tokens:
        if a_token[0] == "aEthUSDC":
            a_usdc = active_network.manifest_named("usdc", address=a_token[1])
        if a_token[0] == "aEthWETH":
            a_weth = active_network.manifest_named("usdc", address=a_token[1])

    starting_usdc_balance = usdc.balanceOf(boa.env.eoa)
    starting_weth_balance = weth.balanceOf(boa.env.eoa)

    print(f"Starting USDC balance: {starting_usdc_balance}")
    print(f"Starting WETH balance: {starting_weth_balance}")
    print(f"Starting aUSDC balance: {a_usdc.balanceOf(boa.env.eoa)}")
    print(f"Starting aWETH balance: {a_weth.balanceOf(boa.env.eoa)}")
    return usdc, weth, a_usdc, a_weth
