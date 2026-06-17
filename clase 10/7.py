class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100
        
    def hacer_llamada(self, minutos):
        gasto = minutos * 1
        if self.bateria - gasto < 0:
            print("No tienes suficiente batería.")
        else:
            self.bateria -= gasto
            print(f"Llamada realizada. Batería restante: {self.bateria}%")
            
    def cargar(self):
        self.bateria = 100
        print("El celular se ha cargado al 100%.")

marca_cel = input("Marca del celular: ")
modelo_cel = input("Modelo del celular: ")

mi_cel = Celular(marca_cel, modelo_cel)

tiempo_llamada = int(input("¿Cuántos minutos va a durar la llamada?: "))
mi_cel.hacer_llamada(tiempo_llamada)

quiere_cargar = input("queres poner a cargar el celular? (si/no): ").lower()
if quiere_cargar == "si":
    mi_cel.cargar()