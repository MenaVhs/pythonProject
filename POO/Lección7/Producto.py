class Producto:
    contador_producto = 0

    @classmethod
    def contador_de_producto(cls):
        cls.contador_producto += 1
        return cls.contador_producto

    def __init__(self, nombre, precio):
        self._id_producto = Producto.contador_de_producto()
        self._nombre = nombre
        self._precio = precio

    @property
    def id_producto(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, new_nombre):
        if isinstance(new_nombre, str):
            self._nombre = new_nombre

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, new_precio):
        if isinstance(new_precio, int, float):
            self._precio = new_precio

    def __str__(self):
        return f'ID producto: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}'

if __name__ == '__main__':
    producto1 = Producto('Camisa desde producto', 100.00)
    print(producto1)
    producto2 = Producto('Pantalón desde producto', 333.3)
    print(producto2)



