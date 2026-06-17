with open("datos_seek.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Línea 1: Aprendiendo Python\nLínea 2: Manejo de archivos\nLínea 3: Uso de seek")

with open("datos_seek.txt", "r", encoding="utf-8") as archivo:
    print("1. Leyendo la primera línea")
    print(archivo.readline().strip())
    
    print("\n2. Mostrando el contenido que falta")
    resto = archivo.read()
    print(resto)
    
    print("\n3. Volviendo al inicio con seek(0)")
    archivo.seek(0)
    
    print("\n4. Leyendo todo el archivo de nuevoy completo")
    completo = archivo.read()
    print(completo)