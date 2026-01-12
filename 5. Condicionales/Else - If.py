ingreso_mensual = 72000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit, recorta gastos")
    elif ingreso_mensual - gasto_mensual > 3000:   
        print("Estas bien economicamnete en cualqueier parte del mundo") 
    
elif ingreso_mensual - gasto_mensual > 1000:
    print("Estas bien en Latinoamerica")
    
elif ingreso_mensual - gasto_mensual > 500:
    print("Estas bien en argentina")
    
elif ingreso_mensual - gasto_mensual > 200:
    print("Estas bien en Venezuela")        

else:
    print("Sos pobre")
          
#Elif = else if = en caso contrario, si...             