'''# 59 listas
nombres = ['Juan', 'Carla', 'Mena', 'María']  # Se puede apregar cualquier tipo de dato en una lista
print("1. Lista", nombres)
#  Acceder a los elementos de manera inversa
print("2. Acceder a los elementos de manera inversa", nombres[-2])
# Imprimir un rango
print("3. Imprimir un rango", nombres[0:2])

# Ir del inicio de la lista al índice (sin incluirlo)
print("4. Ir del inicio de la lista al índice (sin incluirlo)",
      nombres[: 3])  # Incluyo todos los índices de la lista hasta el el índice 2 ['Juan'0, 'Carla'1, 'Mena'2]

# desde el índice indicado hasta el final
print("5. esde el índice indicado hasta el final", nombres[1:])

# Cambiar valor
nombres[3] = 'Pedro'
print("Cambiar valor:", nombres)

for nombre in nombres:
      print(nombre)
else:
      print('No hay más ')

#  Largo de una lista
print(len(nombres))
# Agregar un alemento
nombres.append('Lore')
print(nombres)
# insertar un elemento en un índice proportcionado
nombres.insert(1, 'Octavio')
print(nombres)
# Remover un elemento
nombres.remove('Octavio')
print(nombres)
# Remover el último valor agregado
nombres.pop()
print(nombres)
#  Eliminar un elemento en un índice indicado
del nombres[2]
print(nombres)
# Limpiar lista por completo
nombres.clear()
print(nombres)
# Eliminar lista desde RAM
del nombres
print(nombres) # manda error
'''

''''
# Uso de rangos
# Ejercicio 1
num = 11
for i in range(num):
    if i % 3 == 0:
        print(i)
print('Ejercicio 1')
# Ejercicio 2
for i in range(num):
    if 1 < i <= 6:
        print(i)
print('Ejercicio 2')
# Ejercicio 3
for i in range(3, num, 2):
    print(i)
print('Ejercicio 3')
'''

'''
# Una tupla es inmutable, repeta el orden en el que agregan los elementos
frutas = ('Naranja', 'Plátano', 'Guayaba')
# Largo de una tupla
print(len(frutas))
print(frutas)
# acceder a un elemento en particular
print(frutas[0])
# navegación inversa
print(frutas[-2])
# rango de valores
print(frutas[0:1]) # para inidicar que es una tupla, se pone una coma al final del primer índice, sino sería una cadena
print(frutas[0:2]) # sin incluir el último índice
# recorrer los elementos
for fruta in frutas:
    print(fruta, end=' ') # para ver los valores de print: posicionarse en print y dar clic en ctrl + barra de espacio
    
    # para quitar el salto de línea
    # print(fruta, end=' ')

# cambiar el valor de una tupla
# frutas[2] = 'Fresa'
frutaLista = list(frutas) # Conversión de tupla a lista
frutaLista[-2] = 'Pera'
frutas = tuple(frutaLista)
print('\n', frutas)
print(frutas)
# Eliminar la tupla
del frutas
# print(frutas)
'''
'''
# Ejercicio tuplas
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for t in tupla:
    if t < 5:
        lista.append(t)
print(lista)
'''
'''
# Set (conjunto\estructura de datos):
# Set no tiene un orden (no es 0, 1, 2) ni almacenar elmentos duplicados.
# no es posible modificar los elementos almacenados en el set
# pero sí agregar más o eliminarlos

planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
# largo de los elementos
print(len(planetas))
# revisar si un elemento está presente
print('Martes' in planetas)
# agregar más elementos al set
planetas.add('Tierra')
# no soporta duplicados
planetas.add('Tierra')
print(planetas)
# print(planetas) # noo se duplica
# eliminar elementos en caso de que encuentre la llave
planetas.remove('Tierra')
print(planetas)
# otra forma es eliminar elementos, si no se esncunetra el elemento no manda error
planetas.discard('Júpiter')
print(planetas)
# limpiar el set
planetas.clear()
print(planetas)
# eliminar set
del planetas
print(planetas)}
'''

'''
# Diccionarios
# Colección de datos: llave/valor de la llave

# dict(key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Data Base Management System'
}
print(diccionario)
# largo
print(len(diccionario))
# indicar la llave para acceder a un elemnto
print(diccionario['IDE'])
# otra forma
print(diccionario.get('OOP'))
# Modiificar elemento
diccionario['IDE'] = 'Inter dev. Env.'
print(diccionario)
# recorrer elementos
for termino, valor in diccionario.items(): 
    print(termino, valor)
# si sólo quereos recurar los términos
for termino in diccionario.keys():
    print(termino)
# recuperar valores
for valor in diccionario.values():
    print(valor)

# Si hay existencia de un elemento
print('IDe' in diccionario) # falso

# agregar
diccionario['PK'] = 'Primary Key'
print(diccionario)
# remover
diccionario.pop('PK')
print(diccionario)
# limpiar
diccionario.clear()
print('Dic: ', diccionario)
# eliminar
del diccionario
'''