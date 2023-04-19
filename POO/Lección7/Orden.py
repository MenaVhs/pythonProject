from Producto import Producto

class Orden:
    contador_ordenes = 0

    @classmethod
    def contador_de_ordenes(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes
    def __init__(self, productos):
        # Orden.contador_ordenes += 1
        # self._id_orden = Orden.contador_ordenes
        self._id_orden = Orden.contador_de_ordenes()
        self.productos = list(productos) #list(productos) # para que sea una lista

    @property
    def id_orden(self):
        return self._id_orden
    @property
    def productos(self):
        return self._productos
    @productos.setter
    def productos(self, new_producto):
        self._productos = new_producto
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio # valor parcial
        return total
    @staticmethod
    def suma_ordenes(*args):
        total_ordenes = 0
        for arg in args:
            total_ordenes += arg
        return total_ordenes

    def __str__(self):
        productos_str = ''# Almaceno de manera temporal la lista producto
        for producto in self.productos:
            productos_str += producto.__str__() + ' | ' # símbolo de pipe
        return f'Orden: {self.id_orden}, \nProductos: {productos_str}. \nTotal: {Orden.calcular_total(self)}'

if __name__ == '__main__':
    producto1 = Producto('Camisa desde Orden', 100.00)
    producto2 = Producto('Pantalón desde Orden', 333.3)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)

    print(Orden.suma_ordenes(orden1.calcular_total(), orden1.calcular_total()))

