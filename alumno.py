from mongo import DB
from Crud import crud
import json


class Alumno(crud) :
    def __init__(self, nombre=None, apat=None, amat=None, curp=None, matricula=None):
        super().__init__()
        if nombre is None and apat is None and amat is None and curp is None and matricula is None:
            self.list = True
        else:
            self.list = False
        self.nombre = nombre
        self.apat = apat
        self.amat = amat
        self.curp = curp
        self.matricula = matricula
                
                
    

    def __str__(self):
         if self.list:
            return self.mostList()
         else:
            return f"Nombre: {self.nombre}, {self.apat}, {self.amat} Matricula: {self.matricula}"
        
    def getDict(self):
        if self.list:
            return [a.getDict() for a in self.objetos]
        else:
            return {
                "nombre": self.nombre,
                "Ape_Paterno" : self.apat,
                "Ape_Materno" : self.amat,
                "curp" : self.curp,
                "matricula": self.matricula
            }
        
            

    def saveJson(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.getDict(), f, indent=4)
            
    def loadJson(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.toObject(data)
            
    def toObject(self, data):
            for alumnos_data in data:
                grupo = Alumno(alumnos_data['nombre'], alumnos_data['Ape_Paterno'], alumnos_data['Ape_Materno'], alumnos_data['curp'], alumnos_data['matricula'])
                self.agregar_objeto(grupo)


if __name__ == "__main__":
    

    alumno = Alumno("Javier", "Armando", "Garcia", "CURP001", "001")
    alumno2 = Alumno("Roberto", "Cedillo", "Marquez", "CURP002", "002")


    AlumnoLista = Alumno()

    
    AlumnoLista.agregar_objeto(alumno)
    AlumnoLista.agregar_objeto(alumno2)
    #AlumnoLista.agregar_objeto(alumno2)
    print(AlumnoLista)

    