class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = 0
        
    def conducir(self, distancia):
        if distancia > 0:
            self.kilometraje += distancia
            print(f"Has conducido {distancia} km.")
        else:
            print("La distancia debe ser mayor a 0.")
            
    def mostrar_info(self):
        print(f"Coche: {self.marca} {self.modelo} | Kilometraje: {self.kilometraje} km")

marca_auto = input("Introduce la marca del coche: ")
modelo_auto = input("Introduce el modelo del coche: ")

mi_auto = Coche(marca_auto, modelo_auto)

distancia_viaje = float(input("¿Cuántos kilómetros vas a conducir?: "))
mi_auto.conducir(distancia_viaje)
mi_auto.mostrar_info()