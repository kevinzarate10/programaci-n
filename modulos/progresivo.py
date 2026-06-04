import time

horas = int(input("Ingrese horas: "))
minutos = int(input("Ingrese minutos: "))
segundos = int(input("Ingrese segundos: "))

while True:
    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
    time.sleep(1)
    
    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1
        if minutos == 60:
            minutos = 0
            horas += 1
            if horas == 24:
                horas = 0