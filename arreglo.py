class Arreglo:
    def _init_(self):
        self.arreglos = []

    def imprimir_lista(self):
        return '\n'.join(str(arreglo) for arreglo in self.arreglos)

    def _getitem_(self, index):
        return self.arreglos[index]

    # edita el valor del indice que se especifique
    def _setitem_(self, index, valor):
        self.arreglos[index] = valor

    # regresa el numero de elementos que tiene el array
    def _len_(self):
        return len(self.arreglos)

    # Elimina el elmento del indice que le indiquemos
    def _delitem_(self, index):
        del self.arreglos[index]

    # agrega al array el elemento que se le pasa
    def agregar(self, valor):
        self.arreglos.append(valor)