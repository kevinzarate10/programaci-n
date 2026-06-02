from math import pi
def calcular_area_circulo(radio):
    return pi * (radio ** 2)
entrada_radio = float(input("ingresa el radio del círculo: "))
area_resultado = calcular_area_circulo(entrada_radio)
print(f"el área del círculo con radio {entrada_radio} es: {area_resultado}")