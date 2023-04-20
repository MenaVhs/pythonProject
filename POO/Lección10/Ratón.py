from DispositivoEntrada import Dispositivo_Entrada


class Raton(Dispositivo_Entrada):
    contador = 0
    @staticmethod
    def contador_ratones():
        Raton.contador += 1
        return  Raton.contador
        # print(f'Contador {Raton.contador}')
    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        self.__id_raton = Raton.contador_ratones()
    @property
    def id_raton(self):
        return self.__id_raton
    def __str__(self):
        return (f'Ratón: [Id: {self.id_raton}, Tipo de entrada: {self.tipo_entrada}, Marca: {self.marca}]')


if __name__ == '__main__':
    raton1 = Raton('USB', 'HP')
    raton2 = Raton('BlueTooth', 'LogiTech')
    # print(f'contador: {Raton.contador_ratones()}')
    # print(raton1)
    print(raton1, raton2)
