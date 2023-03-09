#importar web3
from web3 import Web3
# Conectarse a la red Ethereum
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your-api-key'))

# Cargar el ABI del contrato
with open('contract.abi', 'r') as f:
    abi = f.read()

# Cargar el bytecode del contrato
with open('contract.bin', 'r') as f:
    bytecode = f.read()

# Crear un objeto de contrato
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Desplegar el contrato a la red
tx_hash = contract.constructor().transact()

# Esperar a que se mine el contrato
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Obtener la dirección del contrato
contract_address = tx_receipt.contractAddress