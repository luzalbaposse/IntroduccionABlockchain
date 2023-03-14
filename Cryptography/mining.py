#Código de ejemplo en la clase
import datetime
import hashlib

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:
    # Este objeto define el bloque génesis y el bloque actual
    maxNonce = 2**32 # El número máximo de nonce que podemos probar 
    block = Block("Genesis") # Creamos el bloque génesis
    dummy = head = block

    def add(self, block):
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        for n in range(self.maxNonce):
            if block.hash()[0] == '0':
                print(block.hash()[0])
                print(block.hash())
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next