# Los condiconales actuan en consecuencia de una condicion (if = si)

# La estructura basica es: 
# if condicion:
#     codigo a ejecutar si la condicion es verdadera (True)
# else:
#     codigo a ejecutar si la condicion es falsa (False)

contraseña_almacenada = "TomasR"
contraseña_escrita = "Tomas"

if contraseña_almacenada == contraseña_escrita: # Si esta condicion es verdadera
    print("Podes pasar, bienvenido") # Se ejecuta este codigo
else: # Si la condicion es falsa
    print("Contraseña Incorrecta") # Se ejecuta este otro codigo
    print("intente nuevamente") 
    
    
ingreso_mensual = 5000

if ingreso_mensual > 10000:
    print("Estas bien economicamnete en cualqueier parte del mundo") 
    
elif ingreso_mensual < 10000:
      if ingreso_mensual > 1000:
          print("estas masomenos bien, lo justo y necesario")
      else:
          print("Sos pobre")   
    
    
         