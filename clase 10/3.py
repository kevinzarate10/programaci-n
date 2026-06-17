class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
        
    def obtener_promedio(self):
        return sum(self.notas) / len(self.notas)
        
    def aprobo(self):
        return self.obtener_promedio() >= 6

nombre_estudiante = input("Nombre del estudiante: ")
nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))

alumno = Estudiante(nombre_estudiante, [nota1, nota2, nota3])
print(f"Promedio de {alumno.nombre}: {alumno.obtener_promedio():.2f}")
print(f"¿Aprobó?: {alumno.aprobo()}")