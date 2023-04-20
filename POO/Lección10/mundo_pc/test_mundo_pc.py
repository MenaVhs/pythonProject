from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.ratón import Raton
from mundo_pc.teclado import Teclado

monitorCompu1 = Monitor('Asus', 27)
tecladoCompu1 = Teclado('USB', 'Patito')
ratonCompu1 = Raton('USB', 'HP')
computadora1 = Computadora('Mi laptop', monitorCompu1, tecladoCompu1, ratonCompu1)

monitorCompu2 = Monitor('DELL', 27)
tecladoCompu2 = Teclado('BlueTooth', 'Ola')
ratonCompu2 = Raton('USB', 'Chrom')
computadora2 = Computadora('Mi PC', monitorCompu2, tecladoCompu2, ratonCompu2)

monitorCompu3 = Monitor('Alienware', 27)
tecladoCompu3 = Teclado('BlueTooth', 'Alien')
ratonCompu3 = Raton('USB', 'LogiTech')
computadora3 = Computadora('Mi GAMER', monitorCompu3, tecladoCompu3, ratonCompu3)

monitorCompu4 = Monitor('HP', 27)
tecladoCompu4 = Teclado('BlueTooth', 'HP')
ratonCompu4 = Raton('USB', 'HP')
computadora4 = Computadora('Mi HP', monitorCompu4, tecladoCompu4, ratonCompu4)

# Generar listas para cada orden
compus1y2 = [computadora1, computadora2]
compus3y4 = [computadora3, computadora4]
orden1 = Orden(compus1y2)
# orden2 = Orden(compus3y4)
orden1.agregar_computadora(computadora4)

print(orden1)
# print(orden2)