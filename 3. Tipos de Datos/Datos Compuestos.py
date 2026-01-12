# Sumar dos variables
numero = 10
numero += 5
numero += 5
# El operador += sirve para sumar o concatenar dependiendo del tipo de dato que estemos usando

# Concatenar (significa unir) dos cadenas/variables con +
texto = "Hola "
texto2 = "¿Como estas?"
print (numero)
# Es texto + texto2, y obtendremos "Hola ¿Como estas?"

# El resultado sera 20 porque viene sumando todo lo que viene atras linea por linea

# En la lista, cada dato es un elemento, y cada elemento lo podemos llamar

lista = ["Tomas Renggli", "Soy Renggli", True, 1.70]
# Una lista es un tipo de matriz, un conjunto de datos ordenados y modificables, que permite elementos duplicados.
# Si queremos llamar al primer elemento, osea a Tomas Renggli, esta en el indice 0.
# Porque contamos desde el 0 en adelante cada dato

tupla = ("Tomas Renggli", "Soy Renggli", False, 1.70)
# Igual a una lista pero inmodificable.

# Lo importante es que a la hora de mostarr una lista o una tupla, se hace el print de la misma forma (con corchete ej: print(lista[]) o print(tupla[]) )

# Esto SI es valido
lista[3]= "2"

# Esto NO es valido
# tupla [2]= "crack"

# Creando un conjunto SET.
# La diferencia con lista y tupla:
# No se pueden repetir datos, se define en llaves y NO se puede llamar por indice ya que no tienen un orden fijo. Ademas no se pueden modificar sus elementos.

conjunto = {"Renggli", 1.70 , False}

#print(conjunto[3]) -> No puede acceder al elemento por indice ya que no tienen un orden fijo (aunque solo se puede hacer mediante un bucle)
# Y si llegara a repeitr un valor, ese valor a la hora de hacer el print, solo aparecera una vez.

#Por ultimo queda ver el Diccionario (dict)
# Un diccionario es una coleccion de datos desordenada, modificable e indexada.
# Cada dato se almacena en formato key : value (clave : valor)
diccionario = {
    "nombre" : "Tomas Renggli" , 
    "canal" : "TomasR" , 
    "estoy_emocionado" : True , 
    "altura" : 1.70 , 
    "dato_duplicado" : "Tomas R"
}

print(diccionario["altura"] + 2)
print(lista[3])
#Estructura del Diccionario:
# key : value






