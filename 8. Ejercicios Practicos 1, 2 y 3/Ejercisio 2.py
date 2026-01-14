# Consignas

# Suponiendo que cada persona promedio habla 2 palabras por segundo
# 1) Pedirle al usuario que diga cualquier texto real y:
# - a) Cuantas palabras dijo
# - b) Cuanto tardaria en decir esa frase
# - c) 

# 2) Si tarda mas de un minuto:
# - a) Decirle "Para flaco, tampoco te pedi un testamento"
# - b) Si tarda menos de un minuto, decirle "Perfecto, no te explayaste tanto"

# 3) Dalto habla un 30% mas rapido, cuanto tardaria en decir la misma frase?

# Datos a tener en cuenta:



# Multiplicar por 100 es mover la coma dos lugares a la derecha (porque el porcentaje es "por cada cien").
# Dividir por 100 es mover la coma dos lugares a la izquierda.
# Para acortar la cantidad de decimales despues de la coma (,), se usa la funcion round(valor, cantidad_de_decimales) o formateo de strings (f"{valor:.2f}").

# Para redondear para arriba un numero, ejemplo 3.2 a 4, se usa la funcion math.ceil(valor) (hay que importar la libreria math primero: import math).   
# Para redondear para abajo un numero, ejemplo 3.8 a 3, se usa la funcion math.floor(valor) (hay que importar la libreria math primero: import math).

# -----------------------------------------------------------------------------------------------------------
                                                              # Resolucion:

# Ejercicio 1:

respuesta_enunciado = "\nLas respuestas son:\n"

persona_promedio = 2 # palabras por segundo
frase_usuario = input("\nDecime cualquier texto real: ")

cant_palabras= len(frase_usuario.split()) # Al poner split(), quiere decir que utilizo el espacio como separador entre palabras
                                          # Entonces, si yo pongo "Hola como estas", el split me va a devolver una lista con ["Hola", "como", "estas"], y al usar len() me va a devolver la cantidad de elementos que hay en esa lista (en este caso 3)
# Tambien podemos hacer regla de 3 simples.
# Si 2 palabras se dicen en 1 segundo,
# "cant_palabras" palabras se dicen en "x" segundos
tiempo_total_segundos = cant_palabras / persona_promedio

resultado1_a = tiempo_total_segundos
resultado1_b = cant_palabras

print(f"\nPerfecto, dijiste {resultado1_b} palabras en un total de {resultado1_a:.2f} segundos.\n")



# -----------------------------------------------------------------------------------------------------------

# Ejercicio 2:

if tiempo_total_segundos > 120:
    resultado2_a = "\nPara flaco, tampoco te pedi un testamento"
    print(resultado2_a)
else:
    # b)
      print("\nPerfecto, no te explayaste tanto\n")

# -----------------------------------------------------------------------------------------------------------

# Ejercicio 3:

print("\nAhora veamos cuanto tardaria Dalto en decir la misma frase...\n")
velocidad_dalto = persona_promedio * 1.3 # Dalto habla un 30% mas rapido
tiempo_dalto_segundos = cant_palabras / velocidad_dalto
resultado3 = tiempo_dalto_segundos
print(f"Dalto tardaria {resultado3:.2f} segundos en decir la misma frase.\n")