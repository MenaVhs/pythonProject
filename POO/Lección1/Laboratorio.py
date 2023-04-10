class Rectángulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def calcular_área(self):
        return self.altura * self.base

class Cubo(Rectángulo):
    def __init__(self, altura, base, volumen):
        super().__init__(altura, base)
        self.volumen = volumen
    def calcular_volumen(self):
        return Rectángulo.calcular_área(self) * self.volumen

altura = float(input('Altura: '))
base = float(input('Base: '))
volumen = float(input('Volumen: '))
areas = Rectángulo(altura, base)
print(f'El área es: {areas.calcular_área()}')

vol = Cubo(altura, base, volumen)
print(f'El volumen es: {vol.calcular_volumen()}')