#independientemente de empleado o generente
from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    print(type(objeto))
    # print(objeto) # manda a llamar el str de la clase POLIMORFISMO
    print(objeto.mostrar_detalles()) # aquí se está sobreescribiendo el método, ya que sólo está
                                    # en la clase padre y aún así se imprime para objetos de la clase hija
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Juan', 2300)
imprimir_detalles(empleado)
gerente = Gerente('Pedro', 13443, 'Finanzas')
imprimir_detalles(gerente)