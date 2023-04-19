from repasoLección7.Producto import Producto

class Orden:
    contador_ordenes = 0

    @classmethod
    def contador_de_ordenes(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, productos):
        self._id_ordenes = Orden.contador_de_ordenes()
        self._productos = list(productos)
    @property
    def id_ordenes(self):
        return self._id_ordenes

    @property
    def productos(self):
        return self._productos
    @productos.setter
    def productos(self, new_productos):
        self._productos = new_productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def __str__(self):
        producto_str = ''
        for producto in self.productos:
            producto_str += producto.__str__() + ' | '
        return f'ID orden: {self.id_ordenes}, \nProductos {producto_str}. \nTotal: {Orden.calcular_total(self)}'

if __name__ == '__main__':
    producto1 = Producto('Lavadora', 120)
    producto2 = Producto('Estuda', 233)

    lista_productos1 = [producto1, producto2]
    orden1 = Orden(lista_productos1)
    print(orden1)