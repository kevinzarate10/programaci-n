cant_menores = 0
cant_mayores = 0

suma_edades_menores = 0
suma_edades_mayores = 0

edad = int(input("Ingrese edad (0-100) o -1 para finalizar: "))

while edad != -1:
    if 0 <= edad <= 100:
        if edad < 18:
            cant_menores += 1
            suma_edades_menores += edad
        else:
            cant_mayores += 1
            suma_edades_mayores += edad
    else:
        print("Edad descartada. Debe estar entre 0 y 100.")
    
    edad = int(input("Ingrese siguiente edad o -1 para finalizar: "))

print("\n" + "="*30)
print("      RESULTADOS")
print("="*30)

if cant_menores > 0:
    promedio_menores = suma_edades_menores / cant_menores
    print(f"Menores de 18 años: {cant_menores}")
    print(f"Promedio de edad: {promedio_menores:.2f}")
else:
    print("No se ingresaron menores de 18 años.")

print("-" * 30)

if cant_mayores > 0:
    promedio_mayores = suma_edades_mayores / cant_mayores
    print(f"Mayores de 18 años: {cant_mayores}")
    print(f"Promedio de edad: {promedio_mayores:.2f}")
else:
    print("No se ingresaron personas de 18 años o más.")