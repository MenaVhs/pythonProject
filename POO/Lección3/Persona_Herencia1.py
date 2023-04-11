class Persona(object):
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str):
            print('Ingrese sólo letras')
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, nueva_edad):
        if not isinstance(nueva_edad, int):
            print('Ingrese un número entero')
        self._edad = nueva_edad

    def __str__(self): # sobreescribiendo sobre la clase padre se escribe en la clase hija
        return f'Persona: {self.nombre} {self.edad}'
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    # sobreescrinir __str__ de Persona para agregarle la información de sueldo
    def __str__(self):
        return f'[Empleado: Sueldo: {self.sueldo}] [{super().__str__()}]'


empleado1 = Empleado('Juan', 34, 3000)