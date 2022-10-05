class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanno):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanno = tamanno

    def __str__(self):
        return f"Id: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamanno}"


if __name__ == "__main__":
    monitor1 = Monitor("Hp", 15)
    print(monitor1)
    monitor2 = Monitor("Acer", 27)
    print(monitor2)