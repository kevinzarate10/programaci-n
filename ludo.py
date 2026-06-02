import random

def pedirEntero():
    while True:
        valor = input("elegi el tamaño del tablero de 5 al 25:")
        if valor != "" and valor.strip().isdigit():
            num = int(valor)
            if 5 <= num <= 25:
                return num

def moverJugador(tablero, nombre, posicion_actual, dado):
    if posicion_actual >= 0 and posicion_actual < len(tablero):
        tablero[posicion_actual] = '_'
    
    if posicion_actual == -1:
        nueva_posicion = dado
    else:
        nueva_posicion = posicion_actual + dado
    
    if nueva_posicion >= len(tablero):
        nueva_posicion = len(tablero) - 1
        
    tablero[nueva_posicion] = nombre
    return nueva_posicion

tamano = pedirEntero()

tablero_j1 = ['_'] * tamano
tablero_j2 = ['_'] * tamano

pos_j1 = -1
pos_j2 = -1

jugando = True

while jugando:
    input("es el turno del jugador numero 1, presionar enter.")
    dado = random.randint(1, 6)
    print(f"dado: {dado}")
    pos_j1 = moverJugador(tablero_j1, 'J1', pos_j1, dado)
    print(f"Jugador J1: {tablero_j1}")
    
    if pos_j1 == tamano - 1:
        print("Ganó Jugador 1!")
        jugando = False
        continue

    input("es el turno del jugador numero 2, presionar enter.")
    dado = random.randint(1, 6)
    print(f"dado: {dado}")
    pos_j2 = moverJugador(tablero_j2, 'J2', pos_j2, dado)
    print(f"Jugador J2: {tablero_j2}")
    
    if pos_j2 == tamano - 1:
        print("gano el jugador numero 2.")
        jugando = False