def esPanvocalica(palabra):
    palabra = palabra.lower()
    
    tiene_a = False
    tiene_e = False
    tiene_i = False
    tiene_o = False
    tiene_u = False
    
    for letra in palabra:
        if letra == 'a':
            tiene_a = True
        elif letra == 'e':
            tiene_e = True
        elif letra == 'i':
            tiene_i = True
        elif letra == 'o':
            tiene_o = True
        elif letra == 'u':
            tiene_u = True

    return tiene_a and tiene_e and tiene_i and tiene_o and tiene_u


while True:
    entrada = input("ingrese una palabra (o escriba 'salir' para terminar): ")
    
    if entrada.lower() == 'salir':
        break
        
    resultado = esPanvocalica(entrada)
    
    print(f"{entrada} es panvolica ? ")
    print(f"{resultado}")