from alumno import Alumno
from grupo import Grupo
from lista import lista

class Carrera(lista):
    def __init__(self, nombre=None,clave=None):
        super().__init__()
        self.nombre = nombre
        self.clave = clave


    def __repr__(self):
        return f'{self.nombre},{self.clave}'

    def agregar_grupo(self, grupo):
        self.agregar(grupo)

if __name__ == '__main__':
    alumno1 = Alumno("Mario", "Garcia", "Rodriguez", "GRCAG554562HCLRSA3", "22122330017")
    grupo1 = Grupo("7mo", "A")
    grupo1.agregarAlumno(alumno1)  # Asegúrate de agregar el alumno al grupo
    carrera1 = Carrera("Tics", "2212")
    carrera1.agregar_grupo(grupo1)

    print(carrera1)  # Imprime la representación de la carrera
    for grupo in carrera1.elementos:  # Accede a los grupos
        print(f"Grupo: {grupo.grado} {grupo.seccion}")
        for alumno in grupo.elementos:  # Usa `elementos` para acceder a los alumnos
            print(alumno)