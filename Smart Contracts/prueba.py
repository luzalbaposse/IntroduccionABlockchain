# Smart Contract hecho con Vyper para ingresar un texto y hashearlo con SHA-256, para enviarlo a una adress y que el que tenga la clave privada de esa adress pueda desbloquear el texto
import vyper
import hashlib
from web3 import Web3
from vyper import compiler
from vyper import ast as vy_ast

# Compilamos el smart contract
vyper_code = open('smartcontract.vy').read()
compiled_code = compiler.compile_code(vyper_code)

# Importamos el smart contract compilado
abi = compiled_code['abi']
bytecode = compiled_code['bytecode']

# Conectamos a la red de Ethereum
w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/...'))

# Definimos la direccion del smart contract
contract_address = Web3.toChecksumAddress('0xf1b997a165D088EF6FA1a0877081524a95f41eDE')
contract = w3.eth.contract(address=contract_address, abi=abi)

# Definimos la direccion de la cuenta que va a desbloquear el texto
account_address = Web3.toChecksumAddress('0xf1b997a165D088EF6FA1a0877081524a95f41eDE')

# Definimos la clave privada de la cuenta que va a desbloquear el texto
account_private_key = '0xf1b997a165D088EF6FA1a0877081524a95f41eDE'
account = w3.eth.account.privateKeyToAccount(account_private_key)

#Definimos el texto a hashear
texto = "hola, qué onda?"

#Convierto a bytes
texto_bytes = bytes(texto, "utf-8")

#Hasheo con SHA-256
hash = hashlib.sha256(texto_bytes).hexdigest()

# Enviamos la transaccion para hashear el texto
transaction = contract.functions.hash_texto(texto, hash).buildTransaction({
    'gas': 1000000,
    'gasPrice': w3.toWei('1', 'gwei'),
    'nonce': w3.eth.getTransactionCount(account_address)
})

# Firmamos la transaccion
signed_txn = account.signTransaction(transaction)

# Enviamos la transaccion
tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

# Esperamos a que se confirme la transaccion
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Enviamos la transaccion para desbloquear el texto
transaction = contract.functions.desbloquear_texto(texto, hash).buildTransaction({
    'gas': 1000000,
    'gasPrice': w3.toWei('1', 'gwei'),
    'nonce': w3.eth.getTransactionCount(account_address)
})


