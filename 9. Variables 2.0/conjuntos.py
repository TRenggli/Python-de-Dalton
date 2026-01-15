# Los conjuntos los podemos crear con la funcion built-in "set()"
conjunto_vacio = set(["dato1", "dato2"])  # Crea un conjunto vacio
print(conjunto_vacio)          # Salida: {'dato1', 'dato2'}
print(type(conjunto_vacio))  # Salida: <class 'set'>

# Otras formas de crear conjuntos:
conjunto = {"dato1", "dato2", "dato3"}  # Usando llaves, separando los elementos por comas
conjunto_con_elemento_repetido = {"dato1", "dato2", "dato1"}  # Conjunto con un elemento repetido   
print(conjunto)                          # Salida: {'dato1', 'dato2', 'dato3'}
print(conjunto_con_elemento_repetido)   # Salida: {'dato1', 'dato2'} (el elemento repetido se elimina automaticamente)
print(type(conjunto))  # Salida: <class 'set'>  
# Los conjuntos son colecciones desordenadas de elementos unicos, lo que significa que no permiten elementos duplicados y no mantienen un orden especifico.

# Y que pasa cuando queremos poner un elemento modificable dentro de otor NO modificable?
conjunto = set(["dato1", ["dato1", "Dato2"]"dato2"])  # Esto no se puede hacer, porque los conjuntos no pueden contener elementos modificables como listas o diccionarios
print(conjunto)          # Salida: {'dato1', 'dato2'}
print(type(conjunto))  # Salida: <class 'set'>


# Repasemos un poco la teoria de los conjuntos:
# - Union: La union de dos conjuntos A y B es un conjunto que contiene todos los elementos de A y B. 
# En Python, se puede realizar la union de conjuntos utilizando el operador | o el metodo union().
conjunto_A = {"dato1", "dato2", "dato3"}
conjunto_B = {"dato1", "dato2", "dato3", "dato4", "dato5"}
# El conjunto A es un subconjunto de B, porque todos los elementos de A estan en B, y B es un superconjunto de A. Depende de como lo mires.

# Para verificar si es un subconjunto o superconjunto, podemos usar los metodos issubset() e issuperset()
es_subconjunto = conjunto_A.issubset(conjunto_B)  # Devuelve True si lo de adentro del parentesis esta contenido en el conjunto que llama al metodo (el conjuntoA llama al metodo)
es_superconjunto = conjunto_B.issuperset(conjunto_A)  # Devuelve True si el conjunto que llama al metodo (conjuntoB) contiene todo lo que esta adentro del parentesis (conjuntoA)

# Tambien podemos usar los operadores <= y >=
es_subconjunto_op = conjunto_A <= conjunto_B  # Devuelve True si el conjunto de la izquierda esta contenido en el de la derecha
es_superconjunto_op = conjunto_B >= conjunto_A  # Devuelve True si el conjunto de la izquierda contiene todo lo que esta en el de la derecha

# Verificar si hay un elemento en comun entre ambos conjuntos:
hay_elemento_comun = not conjunto_A.isdisjoint(conjunto_B)  # Devuelve True si hay al menos un elemento en comun entre ambos conjuntos
hay_elemento_comun_op = not (conjunto_A & conjunto_B == set())  # Usando el operador & para verificar si hay elementos en comun y el == set() para ver si el resultado es un conjunto vacio

# El not antes de todo me va a invertir el resultado, si me daba True tendre un False y viceversa.
# isdisjoint() devuelve True si los conjuntos NO tienen elementos en común (son disjuntos)
# isdisjoint() devuelve False si SÍ tienen elementos en común
# Entonces, si quieres una variable que diga "hay elemento común", necesitas invertir el resultado:

# Ahora si, veamos la union de ambos conjuntos:
# Usando el metodo union()
union_conjuntos_metodo = conjunto_A.union(conjunto_B)
# Usando el operador |
union_conjuntos = conjunto_A | conjunto_B