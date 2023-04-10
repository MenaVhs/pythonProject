class Persona:
    def __init__(self, nombre, apellido, edad): # método tipo dunder: doble subrayado (underscore) al comienzo y al fina
        # Atributo de instancia
        self._nombre = nombre #  "privados" o "convencionalmente privados"
        self._apellido = apellido #  "name mangling" o "enmascaramiento de nombre".
        self._edad = edad

# Decorador
    # Variable de sólo lectura
    @property
    def nombre(self): # Métodos get
        # print('llamando método get nombre')
        return self._nombre

    # Set: acceder al atributo
    @nombre.setter
    def nombre(self, nuevo_nombre):
        # print('llamando método set nombre')
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Nombre: {self.nombre} {self.apellido} de edad: {self.edad}') # se pueden acceder a los atributos sin problema porque está dentro de la clase

    # Método destructor
    def __del__(self):
        print(f'Persona: {self._nombre} {self.apellido} se ha eliminado')
if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 32)
    persona1.mostrar_detalle()
# Cambio de datos a persona 1
    persona1.nombre = 'Pedro'
    persona1.apellido = 'Lara'
    persona1.edad = '55'
    persona1.mostrar_detalle()
print(__name__)
