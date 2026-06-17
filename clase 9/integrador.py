with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Juan,8\n")
    archivo.write("Ana,5\n")
    archivo.write("Pedro,10\n")

with open("notas.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Lucía,7\n")
    archivo.write("Mateo,3\n")

notas = []
alumnos_aprobados = []

with open("notas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            nombre, nota_str = linea.split(",")
            nota = int(nota_str)
            notas.append(nota)
            if nota >= 4:
                alumnos_aprobados.append(nombre)

if notas:
    promedio = sum(notas) / len(notas)
    nota_max = max(notas)
    nota_min = min(notas)
    
    print("ESTADÍSTICAS GENERALES")
    print(f"Promedio general: {promedio:.2f}")
    print(f"Nota más alta: {nota_max}")
    print(f"Nota más baja: {nota_min}")
    
    print("\nALUMNOS APROBADOS:")
    for alumno in alumnos_aprobados:
        print(f"- {alumno}")
else:
    print("No hay datos suficientes para calcular estadísticas.")