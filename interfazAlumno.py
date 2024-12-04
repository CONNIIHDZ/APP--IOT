from alumno import Alumno
from mongo import DB

class InterfazAlumno():
    
   
        def __init__(self, alumnos= None):
            # Inicializar lista objeto 
            mongo = self.ping()
            if mongo and alumnos is None :
                print("Coneccion estbalecida")
                self.mongo = True
                self.alumnos = Alumno()
                self.getOfMongo()
                try:
                    self.getOfJson()
                    self.saveInJson(True)
                    self.saveMongo()
                except:
                    pass
                self.getArchivo = False
            else:
                self.mongo = False
                if alumnos is None:
                        self.getArchivo = True
                        self.alumnos = Alumno()
                    #Verificar si existe el archivo
                        try:
                            self.getOfJson()
                        except:
                            pass
                        
                else:
                        self.mongo = False
                        self.getArchivo = False
                        self.alumnos = alumnos
                
               
            
        def menu(self):
            #self.dropMongo()
            #self.saveMongo()
            if self.getArchivo:
                self.saveInJson()
            print("-----------------Alumno Interfaz-----------------")
            print("Elige una opcion \n 1.Agregar Alumno \n 2.Ver Alumnos \n 3.Borrar Alumno \n 4.Actualizar Alumno \n 5.Salir ")
            case = input("Inserta el numero de la opcion que deseas usar:")
            case = int(case)
            if case == 1:
                self.addAlum()
            elif case == 2:
                self.showALum()
                self.menu()
            elif case == 3:
                self.deletAlum()
            elif case == 4:
                self.updateAlum()
            elif case == 5:
                print("Sesion finalizada.")
            else:
                print("Error!: Opcion no diponible \n Verifique que sea solo un numero \n Verifique que su numero este en las opciones")
                self.menu()
            
        def formAlum(self):
            
            nombre = input("Nombre:")
            apepat = input("Apellido Paterno:")
            apemat = input("Apellido Materno:")
            curp = input("Curp:")
            matr = input("Matricula:")
            
            n_alumno = Alumno(nombre, apepat, apemat, curp, matr)
            return n_alumno
            
        def addAlum(self):
            n_alumno=self.formAlum()
            self.alumnos.agregar_objeto(n_alumno)
            insert=n_alumno.getDict()
            if self.mongo:
                self.saveMongo(insert)
            print("Se agrego de forma exitosa!!")
            
            self.menu()
            
        def showALum(self):
            if not self.alumnos.objetos:
                print("Vacio")
            else:
                print(self.alumnos)
                
        
        def deletAlum(self):
            self.showALum()
            index = input("Indice de alumno que deseas borrar?:")
            index = int(index) - 1
            sec = self.alumnos.__len__()
            
            if sec < index:
                print("No hay alumnos")
            elif index > sec:
                print("Aluno inexistente")
            else:
                self.alumnos.eliminar_objeto(index)
            if self.mongo:
                self.dropMongo()
                self.saveMongo()
            self.menu()
            
            
        def updateAlum(self):
            self.showALum()
            index = input("Indice del alumno que desea editar:")
            n_alumno=self.formAlum()
            index=int(index)-1
            self.alumnos.__setitem__(index, n_alumno) 
            if self.mongo:
                self.dropMongo()
                self.saveMongo()
            print("Se actualizo de forma exitosa!!")
            
            self.menu()
            
        def saveInJson(self, clean=False ):  
            Nombre="Lista_Alumnos.json"
            if clean:
                x=Alumno()
                x.saveJson(Nombre)
            else:
                self.alumnos.saveJson(Nombre)
            
        def getOfJson(self, Nombre="Lista_Alumnos.json"):
            self.alumnos.loadJson(Nombre)
            
        def saveMongo(self, alumno=None):
            conexion= DB("Alumnos")
            if alumno is None:
                data = self.alumnos.getDict()
            else:
                data = alumno
            conexion.insertDoc(data)
            
        def dropMongo(self):
            conexion= DB("Alumnos")
            conexion.deleteAllDocs()    
            
        def getOfMongo(self):
            conexion= DB("Alumnos")
            cargar = conexion.findDoc()
            self.alumnos.toObject(cargar)
            
        def ping(self):
            conexion= DB("Alumnos")
            validar=conexion.ping()
            return validar

if __name__ == "__main__":
    
    alum = Alumno()
    inter = InterfazAlumno()
    inter.menu()