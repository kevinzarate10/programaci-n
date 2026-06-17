class Calculadora:
    def __init__(self):
        pass
        
    def sumar(self, a, b):
        return a + b
        
    def restar(self, a, b):
        return a - b
        
    def multiplicar(self, a, b):
        return a * b
        
    def dividir(self, a, b):
        if b == 0:
            return "Error: No se puede dividir entre cero."
        return a / b

calc = Calculadora()

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    print(f"Resultado: {calc.sumar(num1, num2)}")
elif operacion == "-":
    print(f"Resultado: {calc.restar(num1, num2)}")
elif operacion == "*":
    print(f"Resultado: {calc.multiplicar(num1, num2)}")
elif operacion == "/":
    print(f"Resultado: {calc.dividir(num1, num2)}")
else:
    print("Operación no válida.")