from Orden import Orden
from Producto import Producto



producto1 = Producto('Camisa desde Orden', 100.00)
producto2 = Producto('Pantalón desde Orden', 333.3)
producto3 = Producto('Calsetnies', 23)
producto4 = Producto('Blusa',234)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1) # relación de agregación
# Agregar productos a orden 1
orden1.agregar_producto(producto3) # relación de agregación
orden1.agregar_producto(producto4) # relación de agregación
orden2 = Orden(productos2)
print(orden1)
print(orden2)
suma_ordenes = Orden.suma_ordenes(orden1.calcular_total(), orden2.calcular_total())

print(f'Total de la suma de órdenes: {suma_ordenes}')
