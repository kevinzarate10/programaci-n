def es_alfabetica(palabra):
    palabra = palabra.lower()
    for i in range(len(palabra) - 1):
        if palabra[i] > palabra[i + 1]:
            return False
    return True

entrada_palabra = input("ingrese una palabra: ")

if es_alfabetica(entrada_palabra):
    print(f"la palabra {entrada_palabra} es alfabética.")
else:
    print(f"la palabra {entrada_palabra} no es alfabética.")
