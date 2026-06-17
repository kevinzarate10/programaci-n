class Carrito:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, nombre_producto):
        self.productos.append(nombre_producto)
        print(f"'{nombre_producto}' agregado.")
        
    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            print("Productos en tu carrito:")
            for producto in self.productos:
                print(f"- {producto}")

mi_carrito = Carrito()

while True:
    producto_usuario = input("Introduce un producto para agregar al carrito (o escribe 'salir' para terminar): ")
    if producto_usuario.lower() == 'salir':
        break
    mi_carrito.agregar_producto(producto_usuario)

mi_carrito.mostrar_carrito()