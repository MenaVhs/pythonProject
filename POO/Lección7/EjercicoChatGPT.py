class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.productos):
            raise StopIteration
        producto = self.productos[self.index]
        self.index += 1
        return producto

inventario = Inventario()
producto1 = Producto("Camiseta", 29.99)
producto2 = Producto("Pantalón", 49.99)
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

for producto in inventario:
    print(producto.nombre)