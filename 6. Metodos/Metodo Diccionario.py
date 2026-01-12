diccionario = {
    "nombre" : "Tomas Alejandro",
    "Apellido" : "Renggli",
    "subs" : 10000000 
}

# Nos devolvera todo lo que con tiene el diccionario (con keys y con item podemos iterar)
claves = diccionario.keys()

# Obtendremos lo que vale/significa la variable que querramos buscar
valor_de_kasjdh = diccionario.get("kasjdh")#Si pongo un get el programa aunque no me encuentre lo que yo busque no se trabara y seguira
                                           #Pero si pongo diccionario["kasjdh"] sin el get, al no encontrarlo el programa se va a PARAR
print("Hola papa, el programa continua")

# Eliminando UN elemento del diccionario
diccionario.pop("nombre") #Si quisiera sacar mas elementos, tengo que poner ("elemento" , "elemento2")

# Obtendiendo un elemento de dict_items iterable
diccionario_iterable = diccionario.items()

# Eliminar todo lo del diccionario
diccionario.clear()

#Iterar = Recorrer el elemento. Por ejemplo el diccionario no se puede iterar, es decir, recorrer el elemento (en este caso el diccionario) para poder acceder a CADA UNO de los elementos guardados alli

print(diccionario)
print(diccionario_iterable)