import pytest
from moccasin.config import get_active_network
from script.deposit import get_pool
import boa


@pytest.fixture
def active_network():
    return get_active_network()


@pytest.fixture
def aavev3_pool_address_provider(active_network):
    return active_network.manifest_named("aavev3_pool_address_provider")


@pytest.fixture
def uniswapv3_universal_router(active_network):
    return active_network.manifest_named("uniswapv3_universal_router")


@pytest.fixture
def usdc(active_network):
    return active_network.manifest_named("usdc")


@pytest.fixture
def weth(active_network):
    return active_network.manifest_named("weth")


@pytest.fixture
def pool(aavev3_pool_address_provider):
    return get_pool(aavev3_pool_address_provider)


@pytest.fixture
def account(weth, usdc):
    weth.set_minter(boa.env.eoa, True)
    usdc.set_minter(boa.env.eoa, True)
    return boa.env.eoa
