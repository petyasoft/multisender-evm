DEFAULT_ABI = [
        {
            'constant': True,
            'inputs': [],
            'name': 'name',
            'outputs': [{'name': '', 'type': 'string'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': True,
            'inputs': [],
            'name': 'symbol',
            'outputs': [{'name': '', 'type': 'string'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': True,
            'inputs': [],
            'name': 'totalSupply',
            'outputs': [{'name': '', 'type': 'uint256'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': True,
            'inputs': [],
            'name': 'decimals',
            'outputs': [{'name': '', 'type': 'uint256'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': True,
            'inputs': [{'name': 'who', 'type': 'address'}],
            'name': 'balanceOf',
            'outputs': [{'name': '', 'type': 'uint256'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': True,
            'inputs': [{'name': '_owner', 'type': 'address'}, {'name': '_spender', 'type': 'address'}],
            'name': 'allowance',
            'outputs': [{'name': 'remaining', 'type': 'uint256'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': False,
            'inputs': [{'name': '_spender', 'type': 'address'}, {'name': '_value', 'type': 'uint256'}],
            'name': 'approve',
            'outputs': [],
            'payable': False,
            'stateMutability': 'nonpayable',
            'type': 'function'
        },
        {
            'constant': False,
            'inputs': [{'name': '_to', 'type': 'address'}, {'name': '_value', 'type': 'uint256'}],
            'name': 'transfer',
            'outputs': [], 'payable': False,
            'stateMutability': 'nonpayable',
            'type': 'function'
        }]

class Network:
    def __init__(self,
                 name: str,
                 rpc: str,
                 chain_id: int,
                 eip1559_tx: bool,
                 coin_symbol: str,
                 explorer: str,
                 decimals: int = 18,
                 ):
        self.name = name
        self.rpc = rpc
        self.chain_id = chain_id
        self.eip1559_tx = eip1559_tx
        self.coin_symbol = coin_symbol
        self.decimals = decimals
        self.explorer = explorer

    def __str__(self):
        return f'{self.name}'


Bsc = Network(
    name = 'bsc',
    rpc = "https://rpc.ankr.com/bsc",
    chain_id = 56,
    eip1559_tx = False,
    coin_symbol = "BNB",
    explorer = "https://bscscan.com/"
)

Opbnb = Network(
    name = 'opbnb',
    rpc = "https://opbnb-mainnet-rpc.bnbchain.org",
    chain_id = 204,
    eip1559_tx = True,
    coin_symbol = "OPBNB",
    explorer = "https://mainnet.opbnbscan.com/"
)


Arbitrum = Network(
    name='arbitrum',
    rpc='https://rpc.ankr.com/arbitrum',
    chain_id=42161,
    eip1559_tx=True,
    coin_symbol='ETH',
    explorer='https://arbiscan.io/',
)


Optimism = Network(
    name='optimism',
    rpc='https://rpc.ankr.com/optimism',
    chain_id=10,
    eip1559_tx=True,
    coin_symbol='ETH',
    explorer='https://optimistic.etherscan.io/',
)


Polygon = Network(
    name='polygon',
    rpc='https://rpc.ankr.com/polygon',
    chain_id=137,
    eip1559_tx=True,
    coin_symbol='MATIC',
    explorer='https://polygonscan.com/',
)


Avalanche = Network(
    name='avalanche',
    rpc='https://rpc.ankr.com/avalanche',
    chain_id=43114,
    eip1559_tx=True,
    coin_symbol='AVAX',
    explorer='https://snowtrace.io/',
)


Fantom = Network(
    name='fantom',
    rpc='https://rpc.ankr.com/fantom',
    chain_id=250,
    eip1559_tx=True,
    coin_symbol='FTM',
    explorer='https://ftmscan.com/',
)

Base = Network(
    name='base',
    rpc='https://rpc.ankr.com/base',
    chain_id=534352,
    eip1559_tx=True,
    coin_symbol='NO',
    explorer='https://scrollscan.com/',
)

Scroll = Network(
    name='scroll',
    rpc='https://rpc.ankr.com/scroll',
    chain_id=8453,
    eip1559_tx=True,
    coin_symbol='NO',
    explorer='https://basescan.org/',
)

Ethereum = Network(
    name='ethereum',
    rpc='https://rpc.ankr.com/eth',
    chain_id=1,
    eip1559_tx=True,
    coin_symbol='ETH',
    explorer='https://etherscan.io/',
)

Zksync = Network(
    name='zksync',
    rpc='https://rpc.ankr.com/zksync_era',
    chain_id=324,
    eip1559_tx=True,
    coin_symbol='NO',
    explorer='https://era.zksync.network/',
)

ArbitrumNova = Network(
    name='arbitrum nova',
    rpc='https://rpc.ankr.com/arbitrumnova',
    chain_id=42170,
    eip1559_tx=True,
    coin_symbol='NO',
    explorer='https://nova.arbiscan.io/',
)

Linea = Network(
    name='linea',
    rpc='https://linea.decubate.com',
    chain_id=59144,
    eip1559_tx=True,
    coin_symbol='ETH',
    explorer='https://lineascan.build/',
) 
ZetaChain = Network(
    name = 'zetachain',
    rpc = "https://zetachain-mainnet-archive.allthatnode.com:8545",
    chain_id = 7000,
    eip1559_tx = True,
    coin_symbol = "ZETA",
    explorer = "https://explorer.zetachain.com/"
)


