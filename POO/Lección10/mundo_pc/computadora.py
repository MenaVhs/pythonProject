from mundo_pc.monitor import Monitor
from mundo_pc.ratón import Raton
from mundo_pc.teclado import Teclado


class Computadora:
    contador = 0
    @staticmethod
    def contador_computadora():
        Computadora.contador += 1
        return Computadora.contador
    def __init__(self, nombre, monitor, teclado, raton):
        self.__id_computadora = Computadora.contador_computadora()
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    @property
    def id_computadora(self):
        return self.__id_computadora

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @property
    def monitor(self):
        return self.__monitor
    @monitor.setter
    def monitor(self, new_monitor):
        self.__monitor = new_monitor
    @property
    def teclado(self):
        return self.__teclado
    @teclado.setter
    def teclado(self, new_teclado):
        self.__teclado = new_teclado
    @property
    def raton(self):
        return  self.__raton
    @raton.setter
    def raton(self, new_raton):
        self.__raton = new_raton

    def __str__(self):
        # return f'Computadora: \n{self.nombre} \n\t{Monitor.__str__(self)}, \n\t{Teclado.__str__(self)}, \n\t{Raton.__str__(self)} '
        return f'\n\t{self.nombre}: \n\t\t{self.monitor},\n\t\t{self.teclado},\n\t\t{self.raton}'

if __name__ == '__main__':
    monitorCompu1 = Monitor('Asus', 27)
    tecladoCompu1 = Teclado('USB', 'Patito')
    ratonCompu1 = Raton('USB', 'HP')
    computadora1 = Computadora('Mi laptop', monitorCompu1, tecladoCompu1, ratonCompu1)
    print(computadora1)

    monitorCompu2 = Monitor('DELL', 27)
    tecladoCompu2 = Teclado('BlueTooth', 'Ola')
    ratonCompu2 = Raton('USB', 'Chrom')
    computadora2 = Computadora('Mi PC', monitorCompu2, tecladoCompu2, ratonCompu2)
    print(computadora2)