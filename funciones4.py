def transformar_vocales(frase):
    resultado = ""
    for caracter in frase:
        if caracter in "aeiouaeiouAEIOUáéíóúÁÉÍÓÚ":
            resultado += caracter.upper()
        else:
            resultado += caracter
    return resultado


entrada_texto = input("ingrese una frase para transformar: ")
texto_modificado = transformar_vocales(entrada_texto)
print(texto_modificado)
