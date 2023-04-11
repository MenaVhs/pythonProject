class Figura_Geométrica:
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto

    @property
    def ancho(self):
        return  self.__ancho
    @ancho.setter
    def ancho(self, new_ancho):
        if isinstance(new_ancho, (int, float)):
            self.__ancho = new_ancho

    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self, new_alto):
        if isinstance(new_alto, (int, float)):
            self.__alto = new_alto
        else:
            print(f'Ingrese un entero o flotante')

