
# Creando una lista con "list"
lista= list([2, 1.56, True])

# Devuelve la cantidad de elementos de una lista
cantidad_lista= len(lista)

# Agregando un elemento a una lista
lista.append(78)

# Agregando un elemento a la lista en un INDICE/LUGAR especifico
lista.insert(2, 1.70)

# Agregando VARIOS elementos a una lista (es como que le estoy agregando otra lista, por eso los corchetes adentro de los parentesis)
lista.extend([23, False])

# Eliminando un elemento de una lista poniendo el indice/numero donde estara ese elemento que querremos eliminar
lista.pop(-1) #-1 para eliminar el ultimo, -2 para eliminar el ante ultimo, y asi sucesivamente

# Eliminando un elemento un element de la lista pero por su nombre, enves de por su indice
#lista.remove("hola")

# Ordena los elemento de forma ascendente
lista.sort() # El problema es que esto solo funciona si la lista NO contiene cadenas de texto, solo numeros

# Ordenamos la lista de forma ascendente y despues invierte los lugares de cada elemento
lista.sort(reverse=True) 

# Inviertiendo los elementos de una lista
lista.reverse()
# Invierte los lugares de cada uno

# Eliminando todos los elementos de la lista
#lista.clear()

# Me aparece todas las cosas que podemos hacer con una lista[]
print(dir(lista))

#me aparece todas las cosas que puedo hacer con una Tupla()
print(dir(("dfsdf")))


#print(lista)