texto_prueba = "Python esta bueno\Estoy trabajando con este archivo en el año 2026\nFin del ejercicio"
with open("estadisticas.txt", "w", encoding="utf-8") as archivo:
    archivo.write(texto_prueba)

with open("estadisticas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    
    archivo.seek(0)
    lineas = archivo.readlines()
    num_lineas = len(lineas)
    
    palabras = contenido.split()
    num_palabras = len(palabras)
    
    num_caracteres = len(contenido)

print(f"Cantidad de líneas: {num_lineas}")
print(f"Cantidad de palabras: {num_palabras}")
print(f"Cantidad de caracteres: {num_caracteres}")