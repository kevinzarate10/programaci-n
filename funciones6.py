def sonAnagramas(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    return sorted(p1) == sorted(p2)

primer_palabra = input("ingresa la primera palabra: ")
segunda_palabra = input("ingresa la segunda palabra: ")

resultado = sonAnagramas(primer_palabra, segunda_palabra)

print(f"las palabras que me diste son anagramas entre si? ({primer_palabra}, {segunda_palabra})")
print(f"{resultado}")
