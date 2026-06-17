class Ventilador:
    def __init__(self):
        self.encendido = False
        self.velocidad = 0
        
    def encender(self):
        self.encendido = True
        self.velocidad = 1
        print("El ventilador se prendió.")
        
    def apagar(self):
        self.encendido = False
        self.velocidad = 0
        print("El ventilador se apagó.")
        
    def cambiar_velocidad(self, nueva_velocidad):
        if not self.encendido:
            print("El ventilador está apagado. encendelo primero.")
            return
            
        if 1 <= nueva_velocidad <= 3:
            self.velocidad = nueva_velocidad
            print(f"la velocidad se ha cambiado a {self.velocidad}.")
        else:
            print("Error: La velocidad debe ser un número del 1 al 3.")

v = Ventilador()

opcion = input("queres prender el ventilador? (si/no): ").lower()
if opcion == "si":
    v.encender()
    nueva_vel = int(input("introducí la velocidad deseada (1 al 3): "))
    v.cambiar_velocidad(nueva_vel)
else:
    v.apagar()