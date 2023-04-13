from Rectangulo import Rectángulo
from Cuadrado import Cuadrado

print('Creación de objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=10, color='Verde')
# cuadrado1.alto = -10 # Valor erróneo
print(cuadrado1)
print('Creación de objeto rectángulo'.center(50, '-'))
rectángulo1 = Rectángulo(alto=10, ancho=13, color='Rojo')
# rectángulo1.alto = 16 # valor erróneo
print(rectángulo1)
# MRO - Method Resolution Order
print('MRO - Method Resolution Order'.center(50, '-'))
print(Cuadrado.mro())
