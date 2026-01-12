# AND
# El operador AND (y) devuelve True solo si ambos operandos son True.
Resultado = True and True # Ambos deben ser True para que el resultado sea True
Resultado2 = False and True # Uno es False, por lo tanto el resultado es False
Resultado3 = True and False # Uno es False, por lo tanto el resultado es False
Resultado4 = False and False # Ambos son False, por lo tanto el resultado es False


# OR
# El operador OR (o) devuelve True si al menos uno de los operandos es True.
Resultado = True or True # Ambos son True, por lo tanto el resultado es True
Resultado2 = False or True # Uno es True, por lo tanto el resultado es True
Resultado3 = True or False # Uno es True, por lo tanto el resultado es True
Resultado4 = False or False # Ambos son False, por lo tanto el resultado es False

# NOT
# El operador NOT (no) invierte el valor del operando.
Resultado9 = not True # El resultado sera False
# Resultado9 = not 2 == 2 # El resultado sera False porque es falso que 2 no es igual a 2
# Resultado9 = not 2 > 29 # El resultado sera True porque es verdadero que 2 NO es mayor a 29

Resultado10 = not False # El resultado sera True

print(Resultado)