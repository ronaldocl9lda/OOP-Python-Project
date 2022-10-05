from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado
from mundo_pc.orden import Orden

teclado1 = Teclado("HP", "USB")
raton1 = Raton("HP", "USB")
monitor1 = Monitor("HP", 15)
computadora1 = Computadora("HP", monitor1, teclado1, raton1)

teclado2 = Teclado("Acer", "Bluetooh")
raton2 = Raton("Acer", "Bluetooh")
monitor2 = Monitor("Acer", 27)
computadora2 = Computadora("Acer", monitor2, teclado2, raton2)

teclado3 = Teclado("Gamer", "Bluetooth")
raton3 = Raton("Gamer", "Bluetooth")
monitor3 = Monitor("Gamer", "Bluetooth")
computadora3 = Computadora("Lenovo", monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

print(orden1)

orden1.agregar_computadora(computadora3)

print(orden1)