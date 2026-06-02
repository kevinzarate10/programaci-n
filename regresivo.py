import time

horas = int(input("Ingrese horas para el temporizador: "))
minutos = int(input("Ingrese minutos para el temporizador: "))
segundos = int(input("Ingrese segundos para el temporizador: "))

while horas >= 0:
    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
    
    if horas == 0 and minutos == 0 and segundos == 0:
        print("<<<< TIEMPO >>>>")
        break
        
    time.sleep(1)
    
    segundos -= 1
    if segundos < 0:
        segundos = 59
        minutos -= 1
        if minutos < 0:
            minutos = 59
            horas -= 1