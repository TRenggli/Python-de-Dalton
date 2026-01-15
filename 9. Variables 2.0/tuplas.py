# Una forma de crear tuplas es usando la funcion built-in "tuple()"
tupla_vacia = tuple(["dato1", "dato2"])  # Cree una lista y la converti en tupla
print(tupla_vacia)          # Salida: ('dato1', 'dato2')
print(type(tupla_vacia))  # Salida: <class 'tuple'>

# Otras formas de crear tuplas:

tupla = "dato1", "dato2", "dato3"  # Sin usar parentesis, separando los elementos por comas
tupla_con_parentesis = ("dato1", "dato2", "dato3")  # Usando parentesis (la forma mas comun)
tupla_un_elemento = ("dato1",)  # Tupla con un solo elemento (al poner la coma despues del elemento, Python lo reconoce como tupla)

print(tupla)                # Salida: ('dato1', 'dato2', 'dato3')
print(tupla_con_parentesis) # Salida: ('dato1', 'dato2', 'dato3')
print(tupla_un_elemento)    # Salida: ('dato1',)

print(type(tupla))  # Salida: <class 'tuple'>

# Cuando solo vamos a LEER datos y no necesitamos MODIFICARLOS, es recomendable usar tuplas en lugar de listas, ya que las tuplas son inmutables (no se pueden cambiar despues de ser creadas) y pueden ofrecer ventajas en terminos de rendimiento y seguridad de datos.
