# Que es el desempaquetado de Variables?
# El desempaquetado de variables es una forma rapida y sencilla de asignar multiples valores a multiples variables en una sola linea de codigo.
# En lugar de asignar cada valor a una variable individualmente, podemos "desempaquetar" una secuencia de valores directamente en las variables correspondientes.

datos_en_tupla = ("Tomas", "Renggli", 1000000)  # Una tupla con dos elementos
datos_en_lista = ["Tomas", "Renggli", 1000000]  # Una lista con tres elementos
datos_en_Set = {"Tomas", "Renggli", 1000000}  # Un set con tres elementos

nombre, apellido, suscriptores = datos_en_tupla    # Desempaquetado de la tupla en dos variables
nombre, apellido, suscriptores = datos_en_lista    # Desempaquetado de la lista en dos variables

print(suscriptores)  # Salida: 1000000

# Se respeta el orden, es decir, "Tomas" se asigna a "nombre" y "Renggli" a "apellido"