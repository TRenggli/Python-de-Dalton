# Que es un input? 
# Basicamente es pedirle un dato al usuario
# Siempre nos devolvera un dato tipo texto 

nombre = input("Che maestro, dame tu nombre porfavor: ")
numero = input("Che maestro, dame tu edad porfavor: ")

# Convierto un numero entero y lo multiplico por 2
resultado = int(numero) * 2

# Convierto el numero a flotante y lo multiplico por 3.5
resultado_flotante = float(numero) * 3.5

# Mostrando el dato
print(f"El nombre es {nombre}")
print(f"La edad es {numero}")