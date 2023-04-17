class MiClase:
    # Atributo de clase
    variable_clase = 'Valor variable clase'
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

# print(MiClase.variable_clase)
miClase = MiClase('valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

# Variable de clase al vuelo (en cualquier momento)
MiClase.variable_clase2 = 'Valor de Variable Clase 2'

miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase2) # Objeto 2 de mi clase
print(miClase.variable_clase2) # Objeto 1 de mi clase
print(MiClase.variable_clase2) # Clase principal, como la variable se escribió al vuelo, el líder no la reconce pero se puede accdeder a ella