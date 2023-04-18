class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        # Persona.contador_personas += 1
        # self.id_persona = Persona.contador_personas
        self.id_persona = Persona.generar_siguiente_valor() # código límpio
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona}, {self.nombre}, {self.edad}]'

persona1 = Persona('Juan', 32)
print(persona1)
persona2 = Persona('Lalo', 23)
print(persona2)
persona3 = Persona('Mena', 24)
print(persona3)
# Aumentar el número de personas de manera independiente
Persona.generar_siguiente_valor() # incremento de la variable a 4
persona4 = Persona('María', 43)

print(f'Valor contador personas: {Persona.contador_personas}')
