import hashlib

def hash_sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

data = "palabra"
print ("Data: ", data)
print ("Hash: ", hash_sha256(data))
