alumnos = ["Juan", "María", "Pedro", "Ana", "Luis"]
with open("alumnos.txt", "w", encoding="utf-8") as archivo:
    for alumno in alumnos:
        archivo.write(alumno + "\n")

with open("alumnos.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

print("lista de alumnos")
for indice, linea in enumerate(lineas, start=1):
    print(f"{indice}) {linea.strip()}")

print(f"\ntotal de alumnos: {len(lineas)}")