class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

nombre_usuario = input("Introduce tu nombre: ")
edad_usuario = int(input("Introduce tu edad: "))

persona1 = Persona(nombre_usuario, edad_usuario)
persona1.saludar()