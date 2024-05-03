from client import Client
from models import Bsc
from models import Opbnb
from models import Arbitrum
from models import Optimism
from models import Polygon
from models import Avalanche
from models import Fantom
from models import Base
from models import Scroll
from models import Ethereum
from models import Zksync
from models import ArbitrumNova
from models import Linea
from models import ZetaChain

def main():
    NATIVE_VALUE = 0.00000001
    GWEI = 1  #if you are sure that the transaction will go through, else GWEI = None
    PRIVATE_KEY = "PRIVATE_KEY"
    with open("addresses.txt") as file:
        wallets = [acc.strip() for acc in file.readlines()]
        
    client = Client(private_key=PRIVATE_KEY, network=Bsc)
    
    for wallet in wallets:
        try:
            answer = client.send_transaction(to = wallet, value = NATIVE_VALUE, GWEI=GWEI)
            client.verif_tx(tx_hash=answer)
            print(f"SUSSECC SEND TO {wallet} tx : {answer}\n\n")
        except Exception as err:
            print(client.address,err)
    
if __name__ == "__main__":
    main()
