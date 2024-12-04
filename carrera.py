from grupo import Grupo
from alumno import Alumno
import json
from Crud import crud

class Carrera(crud):
    def __init__(self, nombre=None, clave=None, grupos=None):

            super().__init__()
            if nombre is None:
                self.list = True
            else:
                self.list = False
            self.nombre = nombre
            self.clave = clave
            self.grupos = grupos
        
    def __str__(self):
        if self.list:
            return self.mostList()
        else:
            return f"Carrera: {self.nombre}, Clave: {self.clave}, Grupos:\n{self.grupos}"
        
        
    def getDictC(self):
        if self.list:
            return [g.getDictC() for g in self.objetos]
        else:
            return {
                "nombre": self.nombre,
                "clave" : self.clave,
                "grupos" : self.grupos.getDictG()
            }
        

        
    def saveJson(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.getDictC(), f, indent=4)
            
                
    def loadJsonC(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.toObject(data)
            
    def toObject(self, data):
            for carrera_data in data:
                grupos = Grupo()
                grupos.toObject(carrera_data['grupos'])                
                carrera = Carrera(carrera_data['nombre'], carrera_data['clave'], grupos)
                self.agregar_objeto(carrera)
        

if __name__ == "__main__":
    
    
    loadcarrera = Carrera()
    
    loadcarrera.loadJsonC("carreraCarga.json")
    
    print(loadcarrera)
    
    
    