from Monitor import Monitor
from Ratón import Raton
from Teclado import Teclado


class Computadora:
    contador = 0
    @staticmethod
    def contador_computadora():
        Computadora.contador += 1
        return Computadora.contador
    def __init__(self, nombre, monitor, teclado, raton):
        self.__id_computadora = Computadora.contador_computadora()
        self.__nombre = nombre
        self.__monitor = list(monitor)
        self.__teclado = list(teclado)
        self.__raton = list(raton)

    @property
    def id_computadora(self):
        return self.__id_computadora

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
