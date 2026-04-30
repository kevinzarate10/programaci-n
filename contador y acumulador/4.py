numero = int(input("Ingrese un número entero para calcular su factorial: "))

if numero < 0:
    print("Error: El número debe ser mayor o igual a 0.")
else:
    factorial = 1
    i = 1
    
    while i <= numero:
        factorial = factorial * i
        i = i + 1
    
    print(f"El factorial de {numero} es: {factorial}")