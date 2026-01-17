# Creando las listas para los ejemplos
frutas = ["manzana", "banana", "cereza", "durazno", "mango", "pera", "uva", "kiwi", "fresa", "naranja"]
cadena = "HolaDalto"
numeros = [2, 5, 8, 10]

# Saltar una iteracion por x motivo y que siga con la siguiente
for fruta in frutas:
    if fruta == "granada":
        continue # Si encuentra "granada", salta esa iteracion y sigue con la siguiente
    print("Me gusta comer " + fruta)

# Evitar que el bucle se ejecute completamente al encontrar un valor especifico
for fruta in frutas:
    print("Fruta: " + fruta)
    if fruta == "pera":
        break # Si encuentra "pera", detiene el bucle completamente, el else tampoco se ejecuta

else:   
    print("Bucle detenido")
    
# Recorrer una cadena de texto con un bucle for (aca recorremos caracter por caracter)
for letra in cadena:
    print(f"El caracter es:{letra}")
    
# Usando un for con una SOLA linea de codigo:
numeros_duplicados = {x**2 for x  in numeros} # La x con los dos asterisco significa que estamos elevando al cuadrado el valor de x