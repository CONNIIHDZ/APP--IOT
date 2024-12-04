from grupo import Grupo
from alumno import Alumno
from carrera import Carrera
from InterfazGrupo import interfazGrupo
from mongo import DB
class InterfazCarrera:
    
   
        def __init__(self, carreras= None):
            mongo = self.ping()
            if mongo and carreras is None:
                print("Coneccion estbalecida")
                self.mongo = True
                self.carreras = Carrera()
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
                if carreras is None:
                    self.getArchivo = True
                    self.carreras = Carrera()
                    try:
                        self.getOfJson()
                    except:
                        pass
                    
                else:
                    self.getArchivo = False
                    self.carreras = carreras
                
            
            
        def menu(self):
            if self.getArchivo:
                self.saveInJson()#Actualizador
            print("")
            print("Elige una opcion \n 1.Agregar \n 2.Ver \n 3.Borrar \n 4.Actualizar \n 5.Salir ")
            case = input("Que opcion que deseas usar:")
            case = int(case)
            if case == 1:
                self.addCarrera()
            elif case == 2:
                self.showCarrera()
                self.menu()
            elif case == 3:
                self.deletCarrera()
            elif case == 4:
                self.updateCarrera()
            elif case == 5:
                 print("finalizado.")
            else:
                print("Error!: Opcion no diponible")
                self.menu()
            
        def formCarrera(self):
            
            carrera = input("Carrea:")
            clave = input("Clave:")
            insert = input("Quieres otro grupo?:(1.Sí/2.NO):")
            if insert == "1":
                grupo = Grupo()
                grupos = interfazGrupo(grupo)
                grupos.menu()
                ngrupos = grupos.grupos
            else:
                ngrupos = Grupo()
            
            
            
            nCarrera= Carrera(carrera, clave, ngrupos)
            return nCarrera
        
        def addCarrera(self):
            nCarrera = self.formCarrera()
            self.carreras.agregar_objeto(nCarrera)
            insert = nCarrera.getDictC()
            if self.mongo:
                self.saveMongo(insert)
            print("Se agrego")
            self.menu()
            
        def showCarrera(self):
            if not self.carreras.objetos:
                print("nada")
            else:
                print(self.carreras)
                
            
        
        def deletCarrera(self):
            self.showCarrera()
            index = input("Que carrera deseas borrar?:")
            index = int(index) - 1
            sec = self.carreras.__len__()
            
            if sec < index:
                print("No hay grupos")
            elif index > sec:
                print("Aluno inexistente")
            else:
                self.carreras.eliminar_objeto(index)
            if self.mongo:
                self.dropMongo()
                self.saveMongo()  
            self.menu()
            
            
        def updateCarrera(self):
            self.showCarrera()
            index = input("Indice de la carrera que desea editar:")
            index=int(index)-1
            grado = input("Nombre:")
            seccion = input("Clave:")
            
            insert = input("Deseas modificar grupos?:(1.Sí/2.NO):")
            if insert == "1":
                gpo = self.carreras[index]
                alumnos = interfazGrupo(gpo.grupos)
                alumnos.menu()
                nalum = alumnos.grupos
            else:
                gpo = self.carreras[index]
                nalum = gpo.grupos
                
            nGrupo= Grupo(grado, seccion, nalum)
            self.carreras.__setitem__(index, nGrupo)
            if self.mongo:
                    self.dropMongo()
                    self.saveMongo()
            #print(nalum)
            print("Se actualizo de forma exitosa!!")
            
            self.menu()
            
        def saveInJson(self, clean=False):

            Nombre = "Lista_Carrera.json"
            if clean:
                x = Carrera()
                x.saveJson(Nombre)
            else:
                self.carreras.saveJson(Nombre)
            
            
            
            
        def getOfJson(self):
            Nombre = "Lista_Carrera.json"
            
            self.carreras.loadJsonC(Nombre)
            
        def saveMongo(self, grupo=None):
            conexion= DB("Carreras")
            if grupo is None:
                data = self.carreras.getDictC()
            else:
                data = grupo
            conexion.insertDoc(data)
            
        def dropMongo(self):
            conexion= DB("Carreras")
            conexion.deleteAllDocs()    
            
        def getOfMongo(self):
            conexion= DB("Carreras")
            cargar = conexion.findDoc()
            self.carreras.toObject(cargar)
            
        def ping(self):
            conexion= DB("Carreras")
            validar=conexion.ping()
            return validar 

            
            
if __name__ == "__main__":
    
    prueb = InterfazCarrera()
    prueb.menu()