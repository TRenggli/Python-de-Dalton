# Un metodo es una funcion aplicada a un objeto
# Estructura: dato/variable.metodo()

cadena1 = "HolasoyTomas"
cadena2 = "Bienvenido maquinola"

# Convierte todo en Mayuscula
mayusc = cadena1.upper() 

# Convierte todo en Minuscula
minusc = cadena1.lower()

# Convierte solo la PRIMER letra en mayuscula de todo el texto
primer_letra_mayusc = cadena1.capitalize()

# Buscamos una cadena en otra cadena
busqueda_find = cadena1.find("s")
# Si nos devuelve como valor -1, significa que no hay coincidencias


# Buscamos una cadena en otra cadena (diferente metodo)
busqueda_index =  cadena1.index("H")
# La diferencia con el Find, es que el Index nos devuelve una exepcion, osea que nos traba el programa


# Si es numerico devolvemos True, sino devolvemos False
es_numerico = cadena1.isnumeric()

# Si es alfanumerico devolvemos true, sino devolvemos False
es_alfanumerico = cadena1.isalpha()

# Buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("T")

# Contamos coincidencias de una cadena dentro de otra cadena; devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("Hola")
# Nos devuelve 0 si no hay coincidencias

# Contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

# Verificamos si una cadena empieza con una cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("H")

# Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("H")

# Reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("Hola" , "Pete")
# El primer parametro es lo que queremos reemplazar, y el segundo parametro es por lo que lo queremos reemplazar

# Separa una cadena en varias formando una lista con sus elementos
cadena_separada = cadena1.split(",")
# Lo que ponemos dentro del parentesis es el caracter que usamos como separador o divisor



print(cadena_nueva)