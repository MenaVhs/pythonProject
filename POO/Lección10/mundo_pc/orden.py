from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.ratón import Raton
from mundo_pc.teclado import Teclado


class Orden:
    contador = 0

    @staticmethod
    def contador_oden():
        Orden.contador += 1
        return Orden.contador

    def __init__(self, computadoras):
        self.__id_orden = Orden.contador_oden()
        self.__computadoras = list(computadoras)
    @property
    def id_orden(self):
        return self.__id_orden
    @property
    def computadoras(self):
        return self.__computadoras
    @computadoras.setter
    def computadoras(self, new):
        self.__computadoras = new

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadora_str = ''
        for compu in self.computadoras:
            computadora_str += compu.__str__()
        return f'Orden: {self.id_orden}, computadoras: {computadora_str}'

if __name__ == '__main__':
    monitorCompu1 = Monitor('Asus', 27)
    tecladoCompu1 = Teclado('USB', 'Patito')
    ratonCompu1 = Raton('USB', 'HP')
    computadora1 = Computadora('Mi laptop', monitorCompu1, tecladoCompu1, ratonCompu1)


    monitorCompu2 = Monitor('DELL', 27)
    tecladoCompu2 = Teclado('BlueTooth', 'Ola')
    ratonCompu2 = Raton('USB', 'Chrom')
    computadora2 = Computadora('Mi PC', monitorCompu2, tecladoCompu2, ratonCompu2)

    monitorCompu3 = Monitor('Alienware', 27)
    tecladoCompu3 = Teclado('BlueTooth', 'Alien')
    ratonCompu3 = Raton('USB', 'LogiTech')
    computadora3 = Computadora('Mi GAMER', monitorCompu3, tecladoCompu3, ratonCompu3)

    monitorCompu4 = Monitor('HP', 27)
    tecladoCompu4 = Teclado('BlueTooth', 'HP')
    ratonCompu4 = Raton('USB', 'HP')
    computadora4 = Computadora('Mi HP', monitorCompu4, tecladoCompu4, ratonCompu4)

    compus1y2 = [computadora1, computadora2]
    compus3y4 = [computadora3, computadora4]
    orden1 = Orden(compus1y2)
    orden2 = Orden(compus3y4)

    print(orden1)
    print(orden2)
    # orden2 = Orden(computadora2)
    # print(orden2)