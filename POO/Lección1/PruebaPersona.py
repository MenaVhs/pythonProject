from Persona_encapsulamiento_parte2 import Persona
print('Creación de objetos'.center(50,'-'))
persona = Persona('Martha', 'Vital', 34)
persona.mostrar_detalle()

# Destructores, es un recolector de basura
print('Eliminación de objetos'.center(50, '-'))
del persona