# Consignas

# 1) Diferencia en porcentaje entre el curso actual y:
# - a) El mas RAPIDO de otros cursos
# - b) El mas LENTO de otros cursos
# - c) El PROMEDIO de los cursos

# 2) Porcentaje de material inserdible/descartable que se reduce en:
# - a) El PROMEDIO de todos los cursos
# - b) El curso ACTUAL (este curso)

# 3) Ver 10 horas de este curso a cuantas horas de otros cursos equivale?

# Datos a tener en cuenta:

# Promedios de duracion (para el ejercicio 1):
# - Minimo: 2.5Hs
# - Promedio 4Hs
# - Maximo: 7Hs
# - Actual: 1.5 hora y media


# Duracion de crudos en horas (para el ejercicio 2):

# - Curso Promedio: 5
# - Curso Actual: 3.5

# Multiplicar por 100 es mover la coma dos lugares a la derecha (porque el porcentaje es "por cada cien").
# Dividir por 100 es mover la coma dos lugares a la izquierda.
# Para acortar la cantidad de decimales despues de la coma (,), se usa la funcion round(valor, cantidad_de_decimales) o formateo de strings (f"{valor:.2f}").

# Para redondear para arriba un numero, ejemplo 3.2 a 4, se usa la funcion math.ceil(valor) (hay que importar la libreria math primero: import math).   
# Para redondear para abajo un numero, ejemplo 3.8 a 3, se usa la funcion math.floor(valor) (hay que importar la libreria math primero: import math).

# -----------------------------------------------------------------------------------------------------------
                                                              # Resolucion:

# Ejercicio 1:
# Para sacar un porcentaje de diferencia entre dos valores, se usa la siguiente formula:
# 100 - (valor_menor / valor_mayor * 100)
curso_lento = 7
curso_promedio = 4
curso_rapido = 2.5
curso_actual = 1.5

resultado1_a = 100 - (curso_actual / curso_rapido * 100)
resultado1_b = 100 - (curso_actual / curso_lento * 100)
resultado1_c = 100 - (curso_actual / curso_promedio * 100)

# Traducción humana:

# valor_menor / valor_mayor → qué fracción representa el más chico
# × 100 → lo pasás a porcentaje
# 100 - eso → lo que falta → la diferencia

# -----------------------------------------------------------------------------------------------------------

# Ejercicio 2:
# Para sacar el porcentaje de material descartable, se usa la siguiente formula:
# 100 - (valor_menor / valor_mayor * 100)

otros_cursos_prom = 5
curso_dalto = 3.5

resultado2_a = 100 - (curso_promedio / otros_cursos_prom * 100)
resultado2_b = 100 - (curso_actual / curso_dalto * 100)

# Traducción humana:

# valor_menor / valor_mayor → qué fracción representa el más chico
# × 100 → lo pasás a porcentaje
# 100 - eso → lo que falta → la diferencia

# -----------------------------------------------------------------------------------------------------------

# Ejercicio 3:
# Para sacar a cuantas horas de otro curso equivale ver 10 horas de este curso, se usa la siguiente formula:
# (valor_actual / valor_otro_curso) * 10
resultado3 = (curso_promedio / curso_actual) * 10

# -----------------------------------------------------------------------------------------------------------

respuesta_enunciado = "\nLas respuestas son:\n"

print(respuesta_enunciado)
print(f"1a) El curso actual es un {resultado1_a:.2f}% mas rapido que el curso mas rapido.")
print(f"1b) El curso actual es un {resultado1_b:.2f}% mas rapido que el curso mas lento.")
print(f"1c) El curso actual es un {resultado1_c:.2f}% mas rapido que el curso promedio.\n")

print(f"2a) El porcentaje de material descartable en el promedio de los cursos es de {resultado2_a:.2f}%.")
print(f"2b) El porcentaje de material descartable en el curso actual es de {resultado2_b:.2f}%.\n")

print(f"3) Ver 10 horas de este curso equivale a {resultado3:.2f} horas en otros cursos.")