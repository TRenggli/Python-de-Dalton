# Iterar significa recorrer cada uno de los elementos de una coleccion (lista, tupla, diccionario, conjunto, etc) uno por uno

# Recordemos que elementos son iterables:
# - conjunto
# - Tuplas
# - Diccionarios
# - Conjuntos
# - Cadenas de texto (strings)
# - Rango de numeros (range)
# - Archivos
# - Etc

# Recordemos que elementos NO son iterables:
# - Numeros enteros (int)
# - Numeros decimales (float)

# Para iterar en Python, usamos el bucle "for"

# ---------------------------------------------------------------------------------------------------------
# conjunto
# Ejemplo 1:

animales = ["perro", "gato", "loro", "cocodrilo"]
numeros = [1, 2, 3, 4, 5]

for animal in animales:
    print(f"\nAhora la variable es {animal}")
    input("Presiona Enter para continuar...")
    
# animal es una variable temporal que toma el valor de cada elemento de la lista en cada iteracion del bucle
# En la primera iteracion, animal sera "perro"
# En la segunda iteracion, animal sera "gato"
# Y asi sucesivamente hasta recorrer todos los elementos de la lista

# Ejemplo 2:
numeros = [52, 16, 14, 72]

for numero in numeros:
    resultado = numero * 10
    print(f"\nAhora la variable es {resultado}")
    input("Presiona Enter para continuar...")
# En cada iteracion, numero toma el valor de cada elemento de la lista numeros
# Y luego multiplicamos ese valor por 10 y lo guardamos en la variable resultado
# Finalmente, imprimimos el valor de resultado en cada iteracion

# ---------------------------------------------------------------------------------------------------------

# Ahora una pregunta, que pasa si queremos iterar sobre dos conjunto? 
# Podemos hacer dos for juntos, o un for dentro de otro for..pero eso seria ineficiente
# La mejor forma es usar la funcion built-in "zip()"

# Primero las conjunto deben tener la misma cantidad de elementos
animales1 = ["gato", "perro", "loro", "cocodrilo"]
numeros1 = [52, 16, 14, 72]

for numero , animal in zip(animales1, numeros1): # numero y animal son variables temporales que toman los valores de cada elemento de las conjunto en cada iteracion
                                                 # y lo que esta adentro del zip() son las dos conjunto que queremos iterar, su orden es importante porque la primera lista sera la que tome la variable numero y la segunda lista sera la que tome la variable animal
    print(f"Recorriendo la lista 1: El numero es {numero}")
    print(f"Recorriendo la lista 2: El animal es {animal}\n")
    
# zip() combina las dos conjunto en una sola, creando tuplas de elementos correspondientes de cada lista
# En la primera iteracion, numero sera 52 y animal sera "gato" . Lo hace al mismo tiempo
# En la segunda iteracion, numero sera 16 y animal sera "perro" y asi sucesivamente hasta recorrer todos los elementos de ambas conjunto. Por eso tienen que coincidir en la cantidad de elementos (tamaño)

# ---------------------------------------------------------------------------------------------------------

# Forma OPTIMA de recorrer una lista usando enumerate()
numeros3 = [52, 16, 14, 72]
print("\nUsando enumerate():")
for num in enumerate(numeros3):  # enumerate genera una secuencia de tuplas, donde cada tupla contiene un indice y el elemento correspondiente de la lista
        print(type(num))
        indice = num[0] # num es una tupla ahora, y de esta forma nos mostrara uno abajo del otro cada una de las tuplas generadas
        valor = num[1]
        print(f"\nEl indice es {indice} y el valor es {valor}")
        
        # En la primera iteracion, num sera (0, 52)
        # En la segunda iteracion, num sera (1, 16) y asi sucesivamente hasta recorrer todos los elementos de la lista
        
        # Y si solo queremos acceder al indice ponemos print(num[0]) , y si queremos acceder al elemento ponemos print(num[1])

# Otra forma es meter un ELSE dentro del for para que nos muestre un mensaje cuando termine de iterar
for numero in numeros3:
    print(f"\nAhora la variable es {numero}")
    
else: # El else tiene que estar a la misma altura que el for, no adentro del for y se van a ejecutar SIEMPRE despues de que termine de iterar todo el for
    print("\nSe ha terminado de iterar la lista.")