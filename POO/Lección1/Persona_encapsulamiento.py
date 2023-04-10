class Persona:
    def __init__(self, nombre, apellido, edad): # método tipo dunder: doble subrayado (underscore) al comienzo y al fina
        # Atributo de instancia
        self._nombre = nombre #  "privados" o "convencionalmente privados"
        self.__apellido = apellido #  "name mangling" o "enmascaramiento de nombre".
        self.edad = edad

    # modelo en una clase
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.__apellido}, {self.edad}') # como está dentro de la clase Persona, se debe agregar el self

# Decorador
    # Recupera el valor de nombre; _nombre
    @property
    def nombre(self): # Métodos get
        print('llamando método get nombre')
        return self._nombre

    # Set: acceder al atributo
    @nombre.setter
    def nombre(self, nuevo_nombre):
        print('llamando método set nombre')
        self._nombre = nuevo_nombre

persona1 = Persona('juan', 'Perez', 32)
print(persona1.nombre) # Gracias al property, ya no se ocupan los () ya que de manera indirecta se manda a llamar el método y no el atributo
persona1.nombre = 'Pedro'
print(persona1.nombre)
# persona1.__apellido = 'Guitierrez'
# persona1.mostrar_detalle()

# python convierte los métodos y atributos privados con la siguente estructura
#     objeto._NombreClase__NombreAtributoPrivado
print(persona1._Persona__apellido)


###################################################################################
'''
# Ejemplo de chatGPT

class MiClase:
    def __init__(self):
        self.publico = "Atributo público"
        self._convencional_privado = "Atributo convencionalmente privado"
        self.__privado = "Atributo privado"

    def metodo_publico(self):
        print("Método público")

    def _metodo_convencional_privado(self):
        print("Método convencionalmente privado")

    def __metodo_privado(self):
        print("Método privado")


objeto = MiClase()

# Acceso a atributos/métodos públicos
print(objeto.publico)
objeto.metodo_publico()

# Acceso a atributos/métodos convencionalmente privados
print(objeto._convencional_privado)
objeto._metodo_convencional_privado()

# Acceso a atributos/métodos privados (enmascarados)
# Esto generará un AttributeError, ya que el nombre real se enmascara con _MiClase__privado
# print(objeto.__privado)  # Descomentar esta línea para ver el error

# Acceso a atributos/métodos privados utilizando el nombre enmascarado
print(objeto._MiClase__privado)
objeto._MiClase__metodo_privado()
'''
'''
En Python, los atributos y métodos que comienzan con un solo guión bajo (_) 
se consideran como "privados" o "convencionalmente privados", lo que significa 
que se supone que no deben ser accedidos directamente desde fuera de la clase, aunque 
todavía es posible hacerlo. Estos atributos y métodos son tratados como parte de la API 
interna de la clase y no se consideran parte de la API pública. Sin embargo, su acceso no 
está restringido y se puede acceder a ellos desde fuera de la clase si se necesita.

Por otro lado, los atributos y métodos que comienzan con dos guiones bajos (__) 
se consideran "privados" y son sujetos a "name mangling" o "enmascaramiento de nombre". 
Esto significa que el nombre real del atributo o método se modifica por la interpretación 
de Python agregándole un prefijo _NombreClase al principio del nombre. Esto se hace para 
evitar conflictos de nombres en clases derivadas que podrían tener atributos o métodos con 
el mismo nombre. Sin embargo, es importante tener en cuenta que estos atributos y métodos 
todavía pueden ser accedidos desde fuera de la clase utilizando la notación correcta 
de _NombreClase__nombre para acceder al nombre enmascarado.
'''
'''
# sobre los decoradores setters y getters

# Getter
class Circulo:
    def __init__(self, radio):
        self._radio = radio  # Atributo privado

    @property
    def radio(self):
        return self._radio

    @property
    def area(self):
        return 3.1415 * (self._radio ** 2)

circulo = Circulo(5)
print(circulo.radio)  # Acceso a la propiedad radio
print(circulo.area)  # Acceso a la propiedad calculada area


# Setter
class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho  # Atributo privado
        self._alto = alto  # Atributo privado

    @property # definir atributos que se comportan como propiedades de solo lectura
    def ancho(self):
        return self._ancho

    @ancho.setter # permiten aplicar lógica adicional antes de asignar el nuevo valor al atributo
                  # pero su valor se calcula dinámicamente en tiempo de acceso a través de un método de la clase
    def ancho(self, valor):
        if valor < 0:
            raise ValueError("El ancho no puede ser negativo")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor < 0:
            raise ValueError("El alto no puede ser negativo")
        self._alto = valor

    def area(self):
        return self._ancho * self._alto

rectangulo = Rectangulo(5, 10)
print(rectangulo.ancho)  # Acceso a la propiedad ancho
rectangulo.ancho = 7  # Modificación de la propiedad ancho
print(rectangulo.ancho)
print(rectangulo.area())  # Cálculo del área
'''
