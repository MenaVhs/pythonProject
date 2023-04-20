from DispositivoEntrada import Dispositivo_Entrada


class Teclado(Dispositivo_Entrada):
    contador = 0

    @staticmethod
    def contador_teclados():
        Teclado.contador += 1
        return Teclado.contador
    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        self.__id_teclado = Teclado.contador_teclados()

    @property
    def id_teclado(self):
        return self.__id_teclado

    def __str__(self):
        return f'Teclado: [Id: {self.id_teclado}, Tipo de entrada: {self.tipo_entrada}, Marca: {self.marca}]'

if __name__ == '__main__':
    teclado1 = Teclado('USB', 'Patito')
    teclado2 = Teclado('Infrarrojo', 'Sony')
    print(teclado1)

