# Estructura de un diccionario: diccionario = { "key1" : "value1"
diccionario = {
    "nombre" : "Tomas Alejandro",
    "Apellido" : "Renggli",
    "subs" : 10000000 
}
# El diccionario ya tiene indices, pero en ves de ser numeros, son cadenas de texto (strings)
# Para acceder a un valor dentro del diccionario, usamos la key (clave)
print(diccionario["nombre"]) # Accedemos al valor "Tomas Alejandro" usando su key "nombre"

# Nos devolvera todo lo que con tiene el diccionario (con keys y con item podemos iterar)
claves = diccionario.keys()

# Obtendremos lo que vale/significa la variable que querramos buscar
valor_de_kasjdh = diccionario.get("kasjdh")# Si pongo un get el programa aunque no me encuentre lo que yo busque no se trabara y seguira
                                           # Pero si pongo diccionario["kasjdh"] sin el get, al no encontrarlo el programa se va a PARAR
print("Hola papa, el programa continua")

# Eliminando UN solo elemento del diccionario
diccionario.pop("nombre") # Si quisiera sacar mas elementos, tengo que poner ("elemento" , "elemento1" , ...)

# Obtendiendo un elemento de dict_items iterable
diccionario_iterable = diccionario.items()

# Eliminar todo lo del diccionario
diccionario.clear()


# Que es Iterar? 
# Iterar es recorrer el elemento. Por ejemplo el diccionario no se puede iterar, es decir, recorrer el elemento (en este caso el diccionario) para poder acceder a CADA UNO de los elementos guardados alli
# Por ejemplo, si yo quiero acceder a cada uno de los elementos del diccionario, tengo que usar un metodo que me permita iterar, por ejemplo keys() o items()
# Con keys() puedo iterar sobre las claves/keys del diccionario

print(claves)
print(diccionario)
print(diccionario_iterable)