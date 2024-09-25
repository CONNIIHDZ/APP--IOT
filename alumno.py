from lista import lista
class Alumno(lista):
    def __init__(self, nombre = None,ap_materno=None,ap_paterno=None,curp=None,matricula=None):
            super().__init__()
            self.nombre = nombre
            self.ap_materno = ap_materno
            self.ap_paterno = ap_paterno
            self.curp = curp
            self.matricula = matricula

    def __repr__(self):
        return f"{self.nombre}{self.ap_materno}{self.ap_paterno}{self.matricula}"

if __name__ == "__main__":
    alumno1=Alumno("Mario","Garcia","Rodriguez","GRCAG554562HCLRSA3","22122330017")
    alumno2=Alumno("Nicolas","Castaneda","Hernandez","NCH554562HCLMNA5","22170153")
    alumno3=Alumno("Leonardo","Mendez","Lopez","MLL554562HCWRSA4","221708989")
    lista_alumnos=lista()
    lista_alumnos.agregar(alumno1)
    lista_alumnos.agregar(alumno2)
    lista_alumnos.agregar(alumno3)

    print(lista_alumnos)