ingreso_mensual = 72000
gasto_mensual = 80000

# Un elif es basicamente un if dentro de un else, para agregar mas condiciones a evaluar y crerar mas de dos caminos a seguir, osea bucle

# Es como hacer esto:
# if condicion1:
#     codigo a ejecutar si la condicion1 es verdadera (True)
#     else:
#       if condicion2:  

# If anidados (If dentro de un else) y elif combinados
if ingreso_mensual > 10000: # Si tu ingreso mensual es mayor a 10000
    if ingreso_mensual - gasto_mensual < 0:  # Y ademas si tu ingreso mensual menos tu gasto mensual es menor a 0
        print("Estas en deficit, recorta gastos") # Entonces pasa esta condicion, estas en deficit
    elif ingreso_mensual - gasto_mensual > 3000: # En caso contrario, si tu ingreso mensual menos tu gasto mensual es mayor a 3000
        print("Tienes un buen margen de ahorro") # Entonces pasa esta condicion, tienes un buen margen de ahorro
    else: # En caso contrario   
        print("Estas bien economicamnete en cualqueier parte del mundo") # Entonces pasa esta condicion, estas bien economicamnete en cualqueir parte del mundo
    
elif ingreso_mensual - gasto_mensual > 1000: 
    print("Estas bien en Latinoamerica")
    
elif ingreso_mensual - gasto_mensual > 500:
    print("Estas bien en argentina")
    
elif ingreso_mensual - gasto_mensual > 200:
    print("Estas bien en Venezuela")        

else:
    print("Sos pobre")
          
#Elif = else if = en caso contrario, si...   
       