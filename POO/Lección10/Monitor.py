class Monitor:
    contador = 0
    @staticmethod
    def contador_monitores():
        Monitor.contador += 1
        return Monitor.contador

    def __init__(self, marca, tamaño):
        self.__id__monitor = Monitor.contador_monitores()
        if self._validar_string(marca):
            self.__marca = marca
        else:
            self.__marca = ''
        if isinstance(tamaño, int):
            self.__tamaño = tamaño
        else:
            self.__tamaño = 0

    @property
    def id_monitor(self):
        return self.__id__monitor

    @property
    def tamaño(self):
        return self.__tamaño
    @tamaño.setter
    def tamaño(self, new_tamaño):
        self.__tamaño = new_tamaño

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, new_marca):
        self.__marca = new_marca

    def _validar_string(self, string):
        return True if isinstance(string, str) else print('Cambie el valor de', string)
    def __str__(self):
        return f'Monitor: [Id: {self.id_monitor}, Tamaño: {self.tamaño} pulgadas, Marca: {self.marca}]'

if __name__ == '__main__':
    monitor1 = Monitor('Asus', 27)
    print(monitor1)
    monitor2 = Monitor('Huawei', 25)
    print(monitor2)
