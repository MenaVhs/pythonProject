from FiguraGeométrica import Figura_Geométrica as FG
from Color import Color as C

class Rectángulo(FG, C):
    def __init__(self, alto, ancho, color):
        FG.__init__(self, alto, ancho)
        C.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
    def __str__(self):
        return f'Área: [{self.calcular_area()}] {FG.__str__(self)}, {C.__str__(self)}'

