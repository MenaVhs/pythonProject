# condicion = True
#
# while condicion:
#     print('Ejecuutando ciclo while')
# else:
#     print('Fin del ciclo while')
#     print('Fin del ciclo while')

# contador = 0
# while contador < 3:
#     print(contador)
#     contador += 1
# else:
#     print('Fin')

'''
maxNum = 5
count = 0
while count < maxNum:
    print(maxNum)
    maxNum -= 1
else:
    print('Fin')
'''

'''
# 57
cadena = 'Holanda'
for letra in cadena:
    if letra == 'a':
        print(letra)
        break
else:
    print('Fin')'''

# 58 continue
# for i in range(6):
#     if i % 2 == 0:
#         print(f'valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')