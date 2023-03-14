
# La idea es ingresar una palabra, hashearla y encontrar el nounce que le corresponda en relacion a la dificultad que asignemos 
# Entonces, si la dificultad es 3, el hash debe comenzar con 3 ceros
import hashlib

#Defino la palabra a hashear
texto = "Este es todo el don quijote de la mancha: En algun lugar de la mancha cuyo nombre no puedo acordarme..."

#Convierto a bytes
texto_bytes = bytes(texto, "utf-8")

# La dificultad va a ser la cantidad de 0
dificultad = 3

# Nounce inicial
nounce = 0

# Iteramos hasta encontrar un hash con la dificultad deseada
while True:
    # Concatenamos el texto y el contador
    texto_contador = texto_bytes + bytes(str(nounce), "utf-8")
    
    # Calculamos el hash SHA-256 de la cadena concatenada
    hash = hashlib.sha256(texto_contador).hexdigest()
    
    # Verificamos si el hash cumple con la dificultad deseada
    if hash[:dificultad] == "0" * dificultad:
        # Si el hash cumple con la dificultad deseada, imprimimos el nonce y el hash
        print("Nonce encontrado:", nounce)
        print("Hash SHA-256:", hash)
        break
    
    # Hasta que encontremos la dificultad que queremos le vamos sumando 1 al nounce
    nounce += 1
