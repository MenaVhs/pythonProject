from NumerosIdenticosException import NumerosIdenticosException


resultado = None

try:
    # validar dentro del try except
    a = int(input('primer numero: '))
    b = int(input('segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('números idénticos')

    resultado = a / b
# except Exception as e: # variable e de exceptio
#     print(f'Ocurrió un error: {e}')

except ZeroDivisionError as zde: # variable e de exceptio
    print(f'Ocurrió un error: {zde}, {type(zde)}')
except TypeError as te:
    print(f'Ocurrió un error: {te}', {type(te)})

except ValueError as e:
    print(f'Valueerror {e}')
except Exception as e: # la clase más genérica debe ir al final
    print(f'Ocurrió un error: {e}, {type(e)}')

else:
    print('Todo en orden (:')

finally:
    # siempre se ejecuta
    # aviso de un recurso o aviso al usuario de cómo terminó la ejecición2
    print('ejecución del finally')

print('Resultado', resultado)
print("Continue...")


