numero = int(input("Ingrese el número para ver su tabla de multiplicar: "))

suma_total = 0

print(f"\n--- Tabla del {numero} ---")

for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    suma_total += resultado

print("-" * 20)
print(f"La suma de todos los resultados es: {suma_total}")