# interpolación (incluir varibales en una cadena
"""numero = 32
print(f'El número es: {numero}')

# División flotante y entera
numero2 = 5
# FLotante
division = numero / numero2
print(division)

# Entera
division = numero // numero2
print(division)

# Residuo de una división
modulo = numero % numero2
print(f'Modulo {modulo}')"""

# Operadores de asignación
miVariable = 10

miVariable += 1 # reasignación
miVariable -= 2
miVariable *= 2
miVariable //= 3.4
print(miVariable)

# Operadores de comparación
"""a = 4
b = 4
resultado = (a == b)
print(f"Resultado de == : {resultado}")
resultado = a != b
print(f"Resltado de != {resultado}")
resultado = a > b
print(f"Resultado de >: {resultado}")
"""

"""
# Ejercicio 36
a = int(input("Escribe un valor numérico: "))

if a % 2 == 0:
    print(f"{a} Es un número par.")
else:
    print(f"{a} No es número impar")
"""
"""
# 37
edad = int(input('Introduce tu edad: '))
23456 print (veintes)
veintes edad >= 20 and edad < 30
treintas edad >= 30 and edad <40
print (treintas)

if veintes or treintas:
    print('Dentro de rango (20\'s) o (30\'s') # el uso de \ hace que se imprima como: 20's o 30's, caracter de escape
else:
    print("No está dentro del rango de edad")
"""
"""
# Rangos
edad = 13

if (20 <= edad < 30 ) or (30 <= edad < 40):
    print('Dentro de rango (20\'s) o (30\'s')
else:
    print('fuera de rango')
"""

# Ejercicio 38
'''
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))
if num1 > num2:
    print(f'Número 1: {num1} es mayor')
else:
    print(f'Número 2: {num2} es mayor')
'''

# Ejercicio tienda de libros 39
nombreLibro = input('Proporcione el nombre del libro: ')
idLibro = int(input('Proporcione el ID: '))
precioLibro = float(input('Precio del libro: '))
envio = (input('Indica si el envío es gratis con True/False: '))

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto'
print(f'''
    Nombre: {nombreLibro}
    ID: {idLibro}
    Precio: {precioLibro}
    Envío gratuito: {envio}
''')