frases = [
    "Python esta bueno\n",
    "Me gusta usar Python\n",
    "Me gusta jugar al futbol\n",
    "JAVA y Python son lenguajes\n"
    "hoy llueve\n"
]

with open("frases.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(frases)

contador_python = 0

with open("frases.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        if "python" in linea.lower():
            contador_python += 1

print(f"Resultado: La palabra python aparece {contador_python} veces")