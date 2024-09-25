class lista:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def editar(self,indice,elemento):
        if 0 <= indice < len(self.elementos):
            self.elementos[indice] = elemento
        else:
            raise IndexError("error")

    def obtener_elementos(self):
        return self.elementos


    def __repr__(self):
        return str(self.elementos)