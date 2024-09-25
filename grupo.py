from alumno import Alumno
from lista import lista
class Grupo(lista):
    def __init__(self ,grado=None, seccion=None):
            super().__init__()
            self.grado = grado
            self.seccion = seccion


    def __repr__(self):
            return f"{self.grado} {self.seccion}"
    def __str__(self):
        return f"Grupo {self.grado} {self.seccion}"

    def agregarAlumno(self,alumno):
        self.agregar(alumno)

if __name__ == "__main__":
    alumno1 = Alumno("Mario", "Garcia", "Rodriguez","GRCAG554562HCLRSA3","22122330017")

    grupo1 = Grupo("7mo", "A")
    grupo1.agregarAlumno(alumno1)


    print(grupo1)
    for alumno in grupo1.elementos:
        print(alumno)