

class crud:
    def __init__(self): 
        self.objetos = []

    def __getitem__(self, index):
        
        return self.objetos[index]

    def __setitem__(self, index, objeto):
        self.objetos[index] = objeto

    def __len__(self):
        return len(self.objetos)

    def mostList(self):
            if not self.objetos:
                return "No hay objetos en la lista."
            
            return '\n'.join(f"{i + 1}. {str(objeto)}" for i, objeto in enumerate(self.objetos))


    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def eliminar_objeto(self, index):
        if 0 <= index < len(self.objetos):
            del self.objetos[index]
        else:
            print("Índice fuera de rango")

    def listar_objetos(self):
        return [str(objeto) for objeto in self.objetos]
