"""
# 43
condicion = 10

if condicion == True:
    print("Condición verdadera")
elif condicion == False:
    print("Condición falsa")
else:
    print("Condición no reconocida")
"""
'''
# 44
num1 = int(input("Ingresa un valor entre 1 y 3: "))
numeroTexto = ' '
if num1 == 1:
    numeroTexto = 'Número uno'
elif num1 ==  2:
    numeroTexto = 'Número dos'
elif num1 == 3:
    numeroTexto = 'Número tres'
else:
    numeroTexto = 'Valor fuera de rango'

print(f'Número proporcionado: {num1} en texto es {numeroTexto}')
'''

'''
# 45 terniario
condicion = True
print('Condición verdadera ') if condicion else print('Condición falsa')
'''
'''
mes = int(input('Proporciona mes del año (1-12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'

print(f'EL mes {mes} la estación del año es {estacion}')
'''

'''# 48 Ejercicio Etapas de la vida
edad = int(input('Ingresa tu edad'))

if 0 <= edad <= 10:
    print('Infancia')
elif 10 <= edad <= 10:
    print('Adolecencia')
elif 20 <= edad <= 30:
    print('Adultes')
else:
    print('Estapa fuera de rango')'''

'''# 49 Ejercicio de tarea
calif = float(input('Engrese calificación entre 0 y 10: '))
if 9 <= calif <= 10:
    print('A')
elif 8 <= calif < 9:
    print('B')
elif 7 <= calif < 8:
    print('C')
elif 6 <= calif < 7:
    print('D')
elif 0 <= calif < 6:
    print('F')
else:
    print('Fuera')'''

# Ciclos