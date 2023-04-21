try:
    10/0
except Exception as e: # variable e de exceptio
    print(f'Ocurrió un error: {e}')

except ZeroDivisionError as e: # variable e de exceptio
    print(f'Ocurrió un error: {e}')