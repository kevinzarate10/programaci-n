class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
        
    def prestar(self):
        if self.prestado:
            print(f"El libro '{self.titulo}' ya estaba prestado.")
        else:
            self.prestado = True
            print(f"Has pedido prestado '{self.titulo}'.")
            
    def devolver(self):
        if not self.prestado:
            print(f"El libro '{self.titulo}' no estaba prestado.")
        else:
            self.prestado = False
            print(f"Has devuelto '{self.titulo}'.")

titulo_libro = input("Introduce el título del libro: ")
autor_libro = input("Introduce el autor del libro: ")

libro1 = Libro(titulo_libro, autor_libro)

accion = input("¿Qué queres hacer con el libro? (prestar/devolver): ").lower()
if accion == "prestar":
    libro1.prestar()
elif accion == "devolver":
    libro1.devolver()