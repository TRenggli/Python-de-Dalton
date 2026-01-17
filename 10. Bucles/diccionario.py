diccionario = {
    "nombre": "lucas",
    "apellido": "dalto",
    "subs": "1000000"
}

# Recorriendo un diccionario con un bucle for para obtener una clave y su valor con items()
for key in diccionario:  # items() devuelve una lista de tuplas con cada par clave-valor del diccionario
    key
    print(f"La clave es: {key}")


# Recorriendo un diccionario con un bucle for para obtener una clave y su valor con items()
for datos in diccionario.items():  # items() devuelve una lista de tuplas con cada par clave-valor del diccionario
    
    key = datos[0]  # key toma el valor de la clave de la tupla
    value = datos[1]  # value toma el valor del valor de la tupla
    print(f"La clave es: {key} y el valor es {value}")
    
