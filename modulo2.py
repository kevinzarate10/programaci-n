def calcular_raices(a, b, c):
    if a == 0:
        return "no es una ecuación cuadrática (A no puede ser 0)"
        
    disc = b**2 - 4*a*c
    if disc < 0:
        return "si tiene raices"
    
    x1 = (-b + disc**0.5) / (2*a)
    x2 = (-b - disc**0.5) / (2*a)
    return x1, x2

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("tiene raices ?", calcular_raices(a, b, c))
