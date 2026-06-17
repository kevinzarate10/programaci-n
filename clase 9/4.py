with open("agenda.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Juan,123456\n")
    archivo.write("Ana,987654\n")

nuevo_nombre = "Carlos"
nuevo_tel = "555111"

with open("agenda.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_tel}\n")

print("Agenda Telefónica:")
with open("agenda.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        if linea_limpia:
            nombre, telefono = linea_limpia.split(",")
            print(f"Nombre: {nombre} | Teléfono: {telefono}")