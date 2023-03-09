import hashlib
import time
import random

def hash_sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

data = "Bitcoin"
print ("Data: ", data)
print ("Hash: ", hash_sha256(data))

#Merkel Tree
transactions = ["3B", "4C", "5D", "6E", "7F", "8G", "9H", "10I", "11J", "12K", "13L", "14M", "15N", "16O", "17P", "18Q", "19R", "20S", "21T", "22U", "23V", "24W", "25X", "26Y", "27Z"]

#Calculo los hashes
hashes_transactions = [hashlib.sha256(t.encode('utf-8')).hexdigest() for t in transactions]
print("Hashes: ", hashes_transactions)
print()

#Combino los hashes de transacciones adyacentes 
pares_hashes = (hashes_transactions[i]+ hashes_transactions[i+1] for i in range(0, len(hashes_transactions), 2))
print("Pares de hashes: ", list(pares_hashes))
print()

#Calculo los hashes de los pares de hashes y los combino en una lista de hashes
hashes_pares = [hashlib.sha256(p.encode('utf-8')).hexdigest() for p in pares_hashes]
print("Hashes de los pares: ", hashes_pares)
print()

#Calculo el hash de la raiz
hash_raiz = hashlib.sha256(hashes_pares[0].encode('utf-8')).hexdigest()
print("Hash de la raiz: ", hash_raiz)
print()



