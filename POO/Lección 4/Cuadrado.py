from Color import Color as C
from FiguraGeométrica import Figura_Geométrica as FG

class Cuadrado(FG, C):
    def __init__(self, lado, color ):
        # super().__init__()
        FG.__init__(self, lado, lado)
        C.__init__(self, color)
    def calcular_area(self):
        return self.alto * self.ancho # son heredados de la clase padre
