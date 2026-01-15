# Creando diccionarios con diferentes metodos
# Metodo 1: Usando llaves {} 
diccionario1 = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
print(diccionario1)  # Salida: {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
print(type(diccionario1))  # Salida: <class 'dict'>

# Metodo 2: Usando la funcion built-in dict()
diccionario2 = dict(clave1="valor1", clave2="valor2", clave3="valor3")
print(diccionario2)  # Salida: {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
print(type(diccionario2))  # Salida: <class 'dict'>

# Metodo 3: Usando una lista de tuplas
lista_de_tuplas = [("clave1", "valor1"), ("clave2", "valor2"), ("clave3", "valor3")]
diccionario3 = dict(lista_de_tuplas)
print(diccionario3)  # Salida: {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
print(type(diccionario3))  # Salida: <class 'dict'>

# Accediendo a los valores de un diccionario
valor1 = diccionario1["clave1"]
print(valor1)  # Salida: valor1

# Agregando un nuevo par clave-valor
diccionario1["clave4"] = "valor4"
print(diccionario1)  # Salida: {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3', 'clave4': 'valor4'}

# Modificando un valor existente
diccionario1["clave2"] = "nuevo_valor2"
print(diccionario1)  # Salida: {'clave1': 'valor1', 'clave2': 'nuevo_valor2', 'clave3': 'valor3', 'clave4': 'valor4'}

# Eliminando un par clave-valor
del diccionario1["clave3"] # Dentro de los corchetes va el elemento que queremos eliminar
print(diccionario1)  # Salida: {'clave1': 'valor1', 'clave2': 'nuevo_valor2', 'clave4': 'valor4'}

# Verificando si una clave existe en el diccionario     
existe_clave1 = "clave1" in diccionario1
print(existe_clave1)  # Salida: True

existe_clave3 = "clave3" in diccionario1
print(existe_clave3)  # Salida: False

# Obteniendo todas las claves y valores del diccionario
claves = diccionario1.keys()
print(claves)  # Salida: dict_keys(['clave1', 'clave2', 'clave4'])

valores = diccionario1.values()
print(valores)  # Salida: dict_values(['valor1', 'nuevo_valor2', 'valor4'])

# Obteniendo todos los pares clave-valor del diccionario. Los devuelve como tuplas dentro de una lista
# La estructura es: variable.items(aca van los parametros que)
items = diccionario1.items()
print(items)  # Salida: dict_items([('clave1', 'valor1'), ('clave2', 'nuevo_valor2'), ('clave4', 'valor4')])

# Iterando sobre un diccionario
# La estructura del for es: for (un numero o variable que contenga un numero) in (variable que recorreremos):  --> Esto itera sobre las claves
for clave, valor in diccionario1.items():
    print(f"La clave es {clave} y el valor es {valor}")
# Salida:
# La clave es clave1 y el valor es valor1
# La clave es clave2 y el valor es nuevo_valor2
# La clave es clave4 y el valor es valor4
