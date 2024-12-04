import json
from alumno import Alumno
from Crud import crud


class Grupo(crud):
    def __init__(self, grado=None, seccion=None, alumnos=None):
 
            super().__init__()
            if grado is None:
                self.list = True
            else:
                self.list = False
            self.grado = grado
            self.seccion = seccion
            self.alumnos = alumnos
    
    def __str__(self):
        if all([self.grado, self.seccion]):
            return f"{self.grado}, {self.seccion} Alumnos: \n{self.alumnos}"
        else:
            return self.mostList()
   
    def getDictG(self):
        if all([self.grado, self.seccion]):
            return {
                "grado": self.grado,
                "seccion" : self.seccion,
                "alumnos" : self.alumnos.getDict()
            }
        else:
            return [g.getDictG() for g in self.objetos]

        
    def saveJson(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.getDictG(), f, indent=4)
            
                
    def loadJsonG(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.toObject(data)


    def toObject(self, data):
            for grupo_data in data:
                alumnos = Alumno()
                alumnos.toObject(grupo_data['alumnos'])
                grupo = Grupo(grupo_data['grado'], grupo_data['seccion'], alumnos)
                self.agregar_objeto(grupo)

            
if __name__ == "__main__":

    alumno1 = Alumno("Javier", "Armando", "Garcia", "CURP001", "001")
    alumno2 = Alumno("Roberto", "Cedillo", "Marquez", "CURP002", "002")
    alumno3 = Alumno("Octavi", "Paz", "Olive", "CURP003", "003")
    
    alumnolista = Alumno()
    alumnolista2 = Alumno()
    
    alumnolista.agregar_objeto(alumno1)
    alumnolista.agregar_objeto(alumno2)
    alumnolista2.agregar_objeto(alumno3)
    
    grup1 = Grupo("5", "c", alumnolista)
    
    grupo2 = Grupo("1", "a", alumnolista2)
    
    grupolista = Grupo()
    
    grupolista.agregar_objeto(grup1)
    grupolista.agregar_objeto(grupo2)
    
    print(alumnolista)
    
    
    
    



