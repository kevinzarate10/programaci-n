class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
        
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

base_usuario = float(input("Introduce la base del rectángulo: "))
altura_usuario = float(input("Introduce la altura del rectángulo: "))

rect = Rectangulo(base_usuario, altura_usuario)
print(f"Área: {rect.calcular_area()}")
print(f"Perímetro: {rect.calcular_perimetro()}")