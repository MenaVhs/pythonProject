# ABC = Abstract Base Class clase base
from abc import ABC, abstractmethod # el último es un decorador para definir un métod abstracto

class Figura_Geométrica(ABC):
    def __init__(self, alto, ancho):
        if self.__validar_valor(alto):
            self.__alto = alto
        else:
            self.__alto = 0
            print(f'Valor erroneo de {alto}')
        if self.__validar_valor(ancho):
            self.__ancho = ancho
        else:
            self.__ancho = 0
            print(f'Valor erroneo de {ancho}')

    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self, new_ancho):
        if isinstance(new_ancho, (int, float)) and self.__validar_valor(new_ancho):
            self.__ancho = new_ancho
        else:
            print(f'{new_ancho}Ingrese un entero o flotante para ancho y dentro del rango')

    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self, new_alto):
        if isinstance(new_alto, (int, float)) and self.__validar_valor(new_alto):
            self.__alto = new_alto
        else:
            print(f'{new_alto} Ingrese un entero o flotante para alto y dentro del rango')

    # Método abstracto
    @abstractmethod
    def calcular_area(self): # no se calcula área aquí ya que se desconoce qué tipo de figura se le calculará el área
        pass

    def __str__(self):
        return f'Figura: [Alto: {self.__alto}. Ancho: {self.__ancho}]'
    def __validar_valor(self, valor):
        return True if 0 < valor < 10 else False
