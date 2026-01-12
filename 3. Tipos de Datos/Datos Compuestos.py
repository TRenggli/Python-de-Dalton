# En la lista, cada dato es un elemento, y cada elemento lo podemos llamar

lista = ["Tomas Renggli", "Soy Renggli", True, 1.70]
#Si queremos llamar al primer elemento, osea a Tomas Renggli, seria el 0,
#Porque contamos desde el 0 en adelante cada dato

tupla = ("Tomas Renggli", "Soy Renggli", False, 1.70)

#La diferencia entre lista y tupla es que en la segunda no puedo modificar ninguno de los datos que se encuentran dentro de esta

#Esto SI es valido
lista[3]= "2"

#Esto NO es valido
#tupla [2]= "crack"

#Creando un conjunto SET.
# La diferencia con lista y tupla:
# No se pueden repetir datos, en llaves y NO se puede llamar por indice

conjunto = {"Renggli", 1.70 , False}

#print(conjunto[3]) -> No puede acceder al elemento

#Por ultimo queda ver el Diccionario (dict)

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






