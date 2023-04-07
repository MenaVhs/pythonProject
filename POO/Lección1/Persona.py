class Persona:
    # mi_atributo # atributo de la clase
    def __init__(self, nombre, apellido, edad): # método tipo dunder: doble subrayado (underscore) al comienzo y al fina
        # Atributo de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # modelo en una clase
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, {self.edad}') # como está dentro de la clase Persona, se debe agregar el self

# objeto dentro de una clase: tiene atributis en una instancia
persona1 = Persona('juan', 'perez', 32)
persona1.mostrar_detalle()
persona1.telefono = '44432323'
print(persona1.telefono)
# # modificación de atributo
# persona1.nombre, persona1.edad, persona1.apellido = 'Pedro',  32, 'Garza'
# print(f'objeto persona1: {persona1.nombre} {persona1.apellido}, edad de {persona1.edad}')

persona2 = Persona('karla', 'gomez', 30)
persona2.mostrar_detalle()

persona3 = Persona('Marco', 'H', 23)
# Otra forma de mandar a llamar el método
Persona.mostrar_detalle(persona3)