resultado = None
a = '10'
b = 0
try:
    resultado = a / b
# except Exception as e: # variable e de exceptio
#     print(f'Ocurrió un error: {e}')

except ZeroDivisionError as zde: # variable e de exceptio
    print(f'Ocurrió un error: {zde}, {type(zde)}')
except TypeError as te:
    print(f'Ocurrió un error: {te}', {type(te)})
except Exception as e: # la clase más genérica debe ir al final
    print(f'Ocurrió un error: {e}, {type(e)}')

print('Resultado', resultado)
