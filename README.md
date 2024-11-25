# Mox Algorithmic Trading

This is part of the Cyfrin Updraft Vyper Course. 

We teach you how to balance a portfolio using Aave and Uniswap! Running the entire project you'll see:

```
Starting setup script...
Getting atokens, this may take a while...
Starting USDC balance: 100000000
Starting WETH balance: 1000000000000000000
Starting aUSDC balance: 0
Starting aWETH balance: 0
Depositing USD Coin into Aave contract 0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2
Depositing Wrapped Ether into Aave contract 0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2
User account data:
        totalCollateralBase: 346570938000
        totalDebtBase: 0
        availableBorrowsBase: 278435091589
        currentLiquidationThreshold: 8285
        ltv: 8034
        healthFactor: 115792089237316195423570985008687907853269984665640564039457584007913129639935
          
Current percent allocation of USDC: 2.88%
Current percent allocation of WETH: 97.12%
Rebalancing needed!
Target allocation of USDC: 30.00%
Target allocation of WETH: 70.00%
Time to swap!
Let's swap 0.27920575180743146 WETH for at least 892.899917 USDC
Depositing USD Coin into Aave contract 0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2
Depositing Wrapped Ether into Aave contract 0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2
User account data:
        totalCollateralBase: 346237604398
        totalDebtBase: 0
        availableBorrowsBase: 273008351068
        currentLiquidationThreshold: 8150
        ltv: 7885
        healthFactor: 115792089237316195423570985008687907853269984665640564039457584007913129639935
          
Current percent allocation of USDC: 29.93%
Current percent allocation of WETH: 70.07%
```

- [Mox Algorithmic Trading](#mox-algorithmic-trading)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Quickstart](#quickstart)
- [Getting ABIs](#getting-abis)
- [Working with Juypter Notebook](#working-with-juypter-notebook)


# Getting Started

## Prerequisites

- [git](https://git-scm.com/)
  - You'll know you've done it right if you can run `git --version` and see a version number.
- [moccasin](https://github.com/Cyfrin/moccasin)
  - You'll know you've done it right if you can run `mox --version` and get an output like: `Moccasin CLI v0.3.0`

## Installation

```bash
git clone https://github.com/cyfrin/mox-algorithmic-trading-cu
cd mox-algorithmic-trading-cu
```

Then, you'll need to make sure you have the following in a `.env` file or environment variables:

```bash
MAINNET_RPC_URL=xxxx # Alchemy, Infura, or other
ANVIL1_PASSWORD_FILE=xxx # Path to a file with the password for your Anvil1 wallet
```

To setup your `anvil1` wallet, run:

```bash
mox wallet import anvil1
```

And pass in the `anvil1` private key when prompted, it is here

```bash
# NEVER STORE PRIVATE KEYS IN PLAIN TEXT
# This one is ok because it's a well known educational key
0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
```

## Quickstart

```bash
mox test -s
```

Or, for LIVE trading:

```bash
mox run deposit_and_rebalance --network zksync --fork false --account your_account
```

# Getting ABIs

```bash
mox explorer get 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2 --save --name weth
mox explorer get 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 --save --name usdc
mox explorer get 0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45 --save --name uniswap_swap_router
mox explorer get 0x2f39d218133AFaB8F2B819B1066c7E434Ad94E9e --save --name aavev3_pool_address_provider
mox explorer get 0x41393e5e337606dc3821075Af65AeE84D7688CBD --save --name aave_protocol_data_provider
mox explorer get 0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419 --save --name eth_usd_price_feed
mox explorer get 0x8fFfFfd4AfB6115b954Bd326cbe7B4BA576818f6 --save --name usdc_usd_price_feed
```

# Working with Juypter Notebook

```bash
from moccasin import setup_notebook

setup_notebook()
```