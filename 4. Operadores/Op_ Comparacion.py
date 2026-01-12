# Los operadores de comparacion nos devolveran un dato booleano (True o False)
# Se lee de izquierda a derecha
es_igual_que = 5 == 6 # Aqui estamos preguntando si 5 es igual a 6, y la respuesta sera False (falso(0))

distinto_que = 5 != 6 # Aqui estamos preguntando si 5 es distinto a 6, y la respuesta sera True (verdadero(1))

mayor_que = 5 > 6 # Aqui estamos preguntando si 5 es mayor a 6, y la respuesta sera False (falso(0))

menor_que = 5 < 6 # Aqui estamos preguntando si 5 es menor a 6, y la respuesta sera True (verdadero(1))

mayor_o_igual = 5 >= 6 # Aqui estamos preguntando si 5 es mayor o igual a 6, y la respuesta sera False (falso(0))
menor_o_igual = 5 <= 6 # Aqui estamos preguntando si 5 es menor o igual a 6, y la respuesta sera True (verdadero(1))

# Calculos Combinados

a = 5
b = 10
c = 20
comparacion = a + b < c # Primero se suman a + b = 15, y luego se compara si 15 < c (20), lo cual es True (verdadero(1))

# Comparar Usuarios
usuario_de_base_de_datos = "Tomas Renggli" 
usuario_escrito = "Tomas"

print(usuario_de_base_de_datos == usuario_escrito) # Nos devolvera False (falso(0)) porque no son iguales

print(es_igual_que , 
      distinto_que , 
      mayor_que , 
      menor_que , 
      mayor_o_igual , 
      menor_o_igual , 
)
