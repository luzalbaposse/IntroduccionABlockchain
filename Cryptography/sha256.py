import hashlib

# def hash_sha256(data):
#     sha256 = hashlib.sha256()
#     sha256.update(data.encode('utf-8'))
#     return sha256.hexdigest()

# data = "Bitcoin"
# print ("Data: ", data)
# print ("Hash: ", hash_sha256(data))

# Merkle Tree
transactions = ["AB2", "AC6","AD8", "AE1", "AF3", "AG5", "AH7", "AI9", "AJ4", "AK2", "AL6", "AM8", "AN1", "AO3", "AP5", "AQ7", "AR9", "AS4", "AT2", "AU6", "AV8", "AW1", "AX3", "AY5", "AZ7", "BA9", "BB4", "BC2", "BD6", "BE8", "BF1", "BG3", "BH5", "BI7", "BJ9", "BK4", "BL2", "BM6", "BN8", "BO1", "BP3", "BQ5", "BR7", "BS9", "BT4", "BU2", "BV6", "BW8", "BX1", "BY3", "BZ5", "CA7", "CB9", "CC4", "CD2", "CE6", "CF8", "CG1", "CH3", "CI5", "CJ7", "CK9", "CL4", "CM2", "CN6", "CO8", "CP1", "CQ3", "CR5", "CS7", "CT9", "CU4", "CV2", "CW6", "CX8", "CY1", "CZ3", "DA5", "DB7", "DC9", "DD4", "DE2", "DF6", "DG8", "DH1", "DI3", "DJ5", "DK7", "DL9", "DM4", "DN2", "DO6", "DP8", "DQ1", "DR3", "DS5", "DT7", "DU9", "DV4", "DW2", "DX6", "DY8", "DZ1", "EA3", "EB5", "EC7", "ED9", "EE4", "EF2", "EG6", "EH8", "EI1", "EJ3", "EK5", "EL7", "EM9", "EN4", "EO2", "EP6", "EQ8", "ER1", "ES3", "ET5", "EU7", "EV9"]

# Calculo los hashes
hashes_transactions = [hashlib.sha256(t.encode()).hexdigest() for t in transactions]
print("Hashes: ", hashes_transactions)
print()

# Combino los hashes de transacciones adyacentes 
pares_hashes = [hashes_transactions[i] + hashes_transactions[i+1] for i in range(0, len(hashes_transactions)-1, 2)]
print("Hashes pares: ", pares_hashes)
print(type(pares_hashes))

# Calculo los hashes de los pares de hashes y los combino en una lista de hashes
hashes_pares = [hashlib.sha256(p.encode('utf-8')).hexdigest() for p in pares_hashes]
print("Hashes de los pares: ", hashes_pares)
print()

# Calculo el hash de la raiz
hash_raiz = hashlib.sha256(hashes_pares[0].encode('utf-8')).hexdigest()
print("Hash de la raiz: ", hash_raiz)
print()
