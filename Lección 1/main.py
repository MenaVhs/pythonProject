'''
# dar pista para una varibale, no únicamente no almacena un tipo de dato
x: str = 'Hola mundo'
# Referencias de memoria
# print(id(x))
# print(type(x))
# literal de tipo cadena
litaralCadena = "Literal" + " " + "Hola"
print(litaralCadena)
# Concantenar
# print("Esto es una cadena: " + litaralCadena)

# print("Mi grupo favorito es:", litaralCadena)
num1 = "1"
num2 = "1"
num1 = int(num1)
num2 = int(num2)
print(type(num2))
suma = num1 + num2
print("Suma:", suma)
'''
'''
variableBool = False
print(variableBool)
variableBool = 3 > 4
print(variableBool)

if variableBool:
    print("Fue verdadero")
else:
    print("El resultado fue falso")
'''
'''
# Función input para procesar la entrada del usuario
numero1 = input("Escribe número 1: ")
numero2 = input("Escribe número 2: ")
resultado = int(numero1) + int(numero2)
print("Resultado: ", resultado)
print("Adiós!")
'''

titulo = input("Proporciona el título del libro: ")
autor = input("Proporciona el autor del libro: ")
print(titulo, "fue escrito por", autor) # se ocupan comas para agregar espacios entre cadenas de caracteres