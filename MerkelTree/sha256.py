import hashlib
import time
import random

# def hash_sha256(data):
#     sha256 = hashlib.sha256()
#     sha256.update(data.encode('utf-8'))
#     return sha256.hexdigest()

# data = "Bitcoin"
# print ("Data: ", data)
# print ("Hash: ", hash_sha256(data))

#Merkel Tree
transactions = ["1","2","3","4"]

#Calculo los hashes
hashes_transactions = [hashlib.sha256(t.encode()).hexdigest() for t in transactions]
print("Hashes: ", hashes_transactions)
print()

#Combino los hashes de transacciones adyacentes 
pares_hashes = (hashes_transactions[i]+ hashes_transactions[i+1] for i in range(0, len(hashes_transactions), 2))
print(pares_hashes)
print()

#Calculo los hashes de los pares de hashes y los combino en una lista de hashes
hashes_pares = [hashlib.sha256(p.encode('utf-8')).hexdigest() for p in pares_hashes]
print("Hashes de los pares: ", hashes_pares)
print()

#Calculo el hash de la raiz
hash_raiz = hashlib.sha256(hashes_pares[0].encode('utf-8')).hexdigest()
print("Hash de la raiz: ", hash_raiz)
print()



