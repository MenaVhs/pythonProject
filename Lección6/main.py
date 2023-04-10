'''
def mi_funcion(nombre, apellido) -> str :  # parámetros / el -> str es una pista del posible dato que va a regresar la función  (pero es opcional)
    print(f'{nombre} y {apellido}')


# mi_funcion('Jimena', 'García') # argumentos: valor que se envía
# mi_funcion('F','d')

# pista en los argumentos

# def sumar(a:int = 0, b:int=0) -> int: # Esto igual es una pista completa pero, no es necesario
def sumar(a=0, b=0):
    return a + b


print(f'Resultado es: {sumar()}')
print(f'Resultado es: {sumar(2, 8)}')
print('dsfd')
'''

'''
def listar_nombres(*nombres): #* es pq no sabemos cuántos nombres serán, python tomará esto como una tupla
    for nombre in nombres:
        print(nombre)

listar_nombres('safd','sdfaa','gtr','regeg','gw','jyrg3') # se convierte en tupla
listar_nombres(3, 43)
'''
'''
def sumar_valores(*args):
    sumacion = 0
    for valor in args:
        sumacion += valor
    return sumacion # si le dejo como print, deja un None al final

print(sumar_valores(3,6,1))'''

'''
def multiplicar_valores(*args):
    multi = 1
    for valor in args:
        multi *= valor
    return multi
print(multiplicar_valores(2, 2,3))
'''

# def listar_terminos(elemento fijo, *elementos de tupla variables, **discionario de términos variable):
'''
def listar_terminos(**terminos): # recibir un diccionario completo
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listar_terminos(IDE = 'Integrated Developement Enviorement', PK='Primary Key')
listar_terminos(DBMS = 'Data Base Management System')
'''

# Distintos tipos de variables en una función
'''
def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['j', 'k', 'g'] # lista

# desplegar_nombres(nombres)
desplegar_nomrbes('Karlo') # en este punto es una cadena
# desplegar_nomrbes(10) # sólo se podrán iteran cuando se contengan varios valores
desplegar_nomrbes((9,3)) # TUPLA
desplegar_nomrbes([10,5]) # LISTA'''

# Funciones recursivas
'''def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
numero = 3
resultado = factorial(numero)
print(f'Factorial de {numero}: {resultado}')
'''
'''
def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero - 1)
    elif numero == 0:
        return print(0)
    elif numero <= 0:
        print('Valor negativo')


imprimir_numero_recursivo(0)
'''
'''
def calcular_total_pago():
    pago_sin_impuesto = float(input('Ingrese el pago sin impuesto: '))
    impuesto = float(input('Ingrese el inpuesto: '))
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return print(f'Pago total: {pago_total}')
# calcular_total_pago()

def calcular_total_pago2(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total


pago_sin_impuesto = float(input('Ingrese el pago sin impuesto : '))
impuesto = float(input('Ingrese el inpuesto: '))
pago_con_impuesto = calcular_total_pago2(pago_sin_impuesto, impuesto)
# print(pago_con_impuesto)
'''
'''
def convertir_celsius_fahrenheit(celsius):
    return celsius * 1.8 + 32
def convertir_fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

celsius = float(input('Temperatura Celsius: '))
fahrenheit = float(input('Temperatura Fahrenheit: '))
f = convertir_celsius_fahrenheit(celsius)
c = convertir_fahrenheit_celsius(fahrenheit)
print(f'Temperatura {celsius} °C = {f:.2f} °F ')
print(f'Temperatura {fahrenheit} °F = {c:0.2f} °C') # indique que del lado izquierdo no importa el número de dígitos, pero del lado derecho sólo muestra dos
'''


