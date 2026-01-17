# A diferencia del for, el bucle while se ejecuta mientras una condicion sea verdadera

contador = 0  # Inicializamos el contador en 0, es importante inicializar la variable antes del bucle

while contador < 10:  # Mientras el contador sea menor que 10, el bucle se ejecuta
    print(contador)  # Mostramos el valor actual del contador
    contador += 1  # Incrementamos el contador en 1 para evitar un bucle infinito
    
print("Bucle terminado")  # Mensaje que indica que el bucle ha finalizado