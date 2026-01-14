# Metodos que vamos a aplicar a las listas
# Un metodo es una funcion aplicada a un objeto

# Creando una lista con "list"
lista = list([2, 1.56, True])
lista1 = list([2, 1.56, True])

# Devuelve la cantidad de elementos de una lista
cantidad_lista= len(lista)
# Ademas de funcionar para cadenas, funciona para listas y tuplas tambien

# Agregando un elemento a una lista
lista.append(78)

# Agregando un elemento a la lista en un INDICE/LUGAR especifico
lista1.insert(2, 1.70)
# Al agregar, el que antes era el indice 2, ahora pasa a ser el indice 3, y asi sucesivamente

# Agregando VARIOS elementos a una lista (es como que le estoy agregando otra lista, por eso los corchetes adentro de los parentesis)
lista.extend([23, False])
# Es agregar una lista a otra lista, agregando todos sus elementos
# Importante: No se puede agregar una tupla a una lista con este metodo
# Y ademas estos elementos los agrega al final de la lista

# Eliminando un elemento de una lista poniendo el indice/numero donde estara ese elemento que querremos eliminar
lista.pop(-1) 
# -1 para eliminar el ultimo, -2 para eliminar el ante ultimo, y asi sucesivamente

# Eliminando un elemento de la lista pero por su nombre, enves de por su indice
lista.remove("hola")
# Si hay varios elementos con el mismo nombre, elimina el primero que encuentra
# Y si no encuentra el elemento, tira un error y nos detiene el programa

# Ordena los elemento de forma ascendente
lista.sort() 
# El problema es que esto solo funciona si la lista NO contiene cadenas de texto, solo numeros (Los True y los False los toma como 1 y 0 respectivamente)

# Inviertiendo los elementos de una lista
lista.reverse()
# Invierte los lugares de cada uno de los elementos de la lista

# Buscando un elemento en una lista, devolviendo su indice/lugar
elemento_encontrado = lista.index(4)

# Eliminando todos los elementos de la lista
lista.clear()
# El resultado sera una lista vacia, osea lista = []

# Con el dir despues del print, me aparece todas las cosas que podemos hacer con una lista[]
print(dir(lista))
# Si yo no hubiera puesto la variable lista dentro del dir, me apareceria todo lo que podemos hacer con cualquier tipo de dato en python

print(dir(set(["hola", 23, True])))
# Set era un conjunto, y de esta forma podemos ver todo lo que podemos hacer con un set
# Pero solo podemos sacar o agregar elementos, no podemos modificar elementos dentro de un set

# Lo unico que podemos hacer con una TUPLA es contar elementos y buscar elementos (index y count)




print(lista1)