class Aritmetica:
    """
    clase aritmetica para hacer sumas, restas, multiplicaciones, etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5,3)
print(f'Sumar: {aritmetica1.sumar()}')
print(f'Restar: {aritmetica1.restar()}')
print(f'Multiplicar: {aritmetica1.multiplicar()}')
print(f'Dividir: {aritmetica1.dividir():0.2f}')


#  Ejercicio

