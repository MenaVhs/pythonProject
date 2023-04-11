class Vehículo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color
    @color.setter
    def ruedas(self, new_color):
        self._color = new_color

    @property
    def ruedas(self):
        return self._ruedas
    @ruedas.setter
    def ruedas(self, new_ruedas):
        self._ruedas = new_ruedas
    def __str__(self):
        return f'Características: [Color: {self.color}. Tipo de rueda: {self._ruedas}]'
class Coche(Vehículo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, new_velocidad):
        if isinstance(new_velocidad, int):
            self._velocidad = new_velocidad
        else:
            print('Ingrese un número entero para velocidad.')
    def __str__(self):
        return f'Coche: [Velocidad: {self.velocidad} km/hr]. {super().__str__()}'
class Bicicleta(Vehículo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, new_tipo):
        if isinstance(new_tipo, str):
            self._tipo = new_tipo
        else:
            print('Ingrese Texto en Tipo.')

    def __str__(self):
        return f'Bicicleta: [Tipo: {self.tipo}]. {super().__str__()}'