class Dispositivo_Entrada:
    def __init__(self, tipo_entrada, marca):
        if self._validar_string(tipo_entrada):
            self._tipo_entrada = tipo_entrada
        else:
            self._tipo_entrada = ''

        if self._validar_string(marca):
            self._marca = marca
        else:
            self._marca = ''

    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    @tipo_entrada.setter
    def tipo_entrada(self, new):
        self._tipo_entrada = new

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, new_marca):
        self._marca = new_marca

    def _validar_string(self, string):
        return True if isinstance(string, str) else print('Cambie el valor de', string)

if __name__ == '__main__':
    dispositivo_entrada1 = Dispositivo_Entrada('d', 'f')
    print(dispositivo_entrada1.tipo_entrada)
    print(dispositivo_entrada1.marca)