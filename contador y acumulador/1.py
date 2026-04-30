mayor = None
menor = None

print("Ingrese números enteros positivos (o -1 para finalizar):")

while True:
    try:
        num = int(input("Número: "))
        
        if num == -1:
            break
            
        if num < 0:
            print("Por favor, ingrese solo números positivos.")
            continue
        
        if mayor is None or num > mayor:
            mayor = num
            
        if menor is None or num < menor:
            menor = num
            
    except ValueError:
        print("Entrada no válida. Debe ingresar un número entero.")

if mayor is not None:
    print("\n--- Resultados ---")
    print(f"El número mayor ingresado es: {mayor}")
    print(f"El número menor ingresado es: {menor}")
else:
    print("\nNo se ingresaron números válidos.")