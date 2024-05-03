from web3 import Web3
from web3.middleware import geth_poa_middleware
from models import Network,DEFAULT_ABI

class Client:
    DEFAULT_ABI = DEFAULT_ABI
    def __init__(
            self,
            private_key : str, 
            network : Network,
    ):
        self.private_key = private_key 
        self.network = network
        self.w3 = Web3(Web3.HTTPProvider(endpoint_uri = self.network.rpc))
        self.address = Web3.to_checksum_address(self.w3.eth.account.from_key(private_key = private_key).address)
    
    def get_decimals(
            self,
            token_address : str = None
    ) -> int: 
        token_address = Web3.to_checksum_address(token_address)
        
        try:
            return self.w3.eth.contract(
                address = Web3.to_checksum_address(token_address),
                abi = Client.DEFAULT_ABI
            ).functions.decimals().call()
        except:
            raise ValueError("Contract not found")
    
    def balance_of(
        self,
        token_address : str,
        address = None
    ) -> int:
        
        token_address = Web3.to_checksum_address(token_address)
        
        if address  == None:
            address = self.address
        try:
            return self.w3.eth.contract(
                address = Web3.to_checksum_address(token_address),
                abi = Client.DEFAULT_ABI
                ).functions.balanceOf(address).call()
        except:
            raise ValueError("Contract or Address not found")
    
    @staticmethod
    def get_max_priority_fee_per_gas(w3: Web3, block: dict) -> int:
        block_number = block['number']
        latest_block_transaction_count = w3.eth.get_block_transaction_count(block_number)
        max_priority_fee_per_gas_lst = []
        for i in range(latest_block_transaction_count):
            try:
                transaction = w3.eth.get_transaction_by_block(block_number, i)
                if 'maxPriorityFeePerGas' in transaction:
                    max_priority_fee_per_gas_lst.append(transaction['maxPriorityFeePerGas'])
            except Exception:
                continue

        if not max_priority_fee_per_gas_lst:
            max_priority_fee_per_gas = w3.eth.max_priority_fee
        else:
            max_priority_fee_per_gas_lst.sort()
            max_priority_fee_per_gas = max_priority_fee_per_gas_lst[len(max_priority_fee_per_gas_lst) // 2]
        return max_priority_fee_per_gas
    
    def token_symbol(
        self,
        token_address : str
    ) -> str:
        try:
            return self.w3.eth.contract(
                    address = Web3.to_checksum_address(token_address),
                    abi = Client.DEFAULT_ABI
                ).functions.symbol().call() 
        except:
            raise ValueError("Invalid Token contract")
    
    def send_transaction(
        self,
        to,
        data=None,
        from_=None,
        increase_gas=1.2,
        value=None,
        max_priority_fee_per_gas: int = None,
        max_fee_per_gas: int = None,
        GWEI = None,
    ):
        if not from_:
            from_ = self.address

        tx_params = {
            'chainId': self.w3.eth.chain_id,
            'nonce': self.w3.eth.get_transaction_count(self.address),
            'from': Web3.to_checksum_address(from_),
            'to': Web3.to_checksum_address(to),
        }
        if data:
            tx_params['data'] = data
        
        if GWEI != None:
            tx_params['gasPrice'] = int(GWEI*10**9)
        else:
            tx_params['gasPrice'] = self.w3.eth.gas_price

        if value:
            tx_params['value'] = int(value*10**18)

        try:
            tx_params['gas'] = int(self.w3.eth.estimate_gas(tx_params) * increase_gas)

        except Exception as err:
            print(f'{self.address} | Transaction failed | {err}')
            return None

        sign = self.w3.eth.account.sign_transaction(tx_params, self.private_key)
        return (self.w3.eth.send_raw_transaction(sign.rawTransaction)).hex()
    
    def verif_tx(
        self, 
        tx_hash
    ) -> bool:
        
        try:
            data = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
            if 'status' in data and data['status'] == 1:
                print(f'{self.address} | transaction was successful: {tx_hash}')
                return True
            else:
                print(f'{self.address} | transaction failed {data["transactionHash"].hex()}')
                return False
        except Exception as err:
            print(f'{self.address} | unexpected error in <verif_tx> function: {err}')
            return False
    
