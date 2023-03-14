import hashlib

#Defino la palabra a hashear
texto = "hola"

#Convierto a bytes
texto_bytes = bytes(texto, "utf-8")

# La dificultad va a ser la cantidad de 0
dificultad = 3

# Definimos el contador (nonce)
contador = 0

# Iteramos hasta encontrar un hash con la dificultad deseada
while True:
    # Concatenamos el texto y el contador
    texto_contador = texto_bytes + bytes(str(contador), "utf-8")
    
    # Calculamos el hash SHA-256 de la cadena concatenada
    hash = hashlib.sha256(texto_contador).hexdigest()
    
    # Verificamos si el hash cumple con la dificultad deseada
    if hash[:dificultad] == "0" * dificultad:
        # Si el hash cumple con la dificultad deseada, imprimimos el nonce y el hash
        print("Nonce encontrado:", contador)
        print("Hash SHA-256:", hash)
        break
    
    # Si el hash no cumple con la dificultad deseada, incrementamos el contador y seguimos iterando
    contador += 1
