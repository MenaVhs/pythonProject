# sobrecarga es que un mismo operador puede comportarse de diferentes formas
# operador +: depende si es entreros, srt, lista -> sobrecarga

a = 2
b = 3
print(a + b)

a = 'Hola '
b = 'Mundo'
print( a +  b)

a = [1,2,3]
b = ['a', 'b', 'c']
print(a + b)
