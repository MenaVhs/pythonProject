class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otro):
        return f'{self.nombre} {otro.nombre}'
                # obj + obj2
                # obj1_add__(obj2)
    def __sub__(self, other):
        return self.edad - other.edad

persona1 = Persona('Juan', 23)
persona2 = Persona('Carlo', 3)
print(persona1 + persona2)
print(persona1 - persona2)
# print(persona1 - persona2)