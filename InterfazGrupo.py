from grupo import Grupo
from alumno import Alumno
from interfazAlumno import InterfazAlumno
from mongo import DB
class interfazGrupo:
    
    def __init__(self, lista_de_grupos=None):
        conexion_activa = self.verificar_conexion_con_mongo()
        if conexion_activa and lista_de_grupos is None:
            print("Conexión establecida con MongoDB")
            self.conexion_mongo = True
            self.lista_de_grupos = Grupo()  
            self.cargar_desde_mongo()
            try:
                self.cargar_desde_json()
                self.guardar_en_json(True)
                self.guardar_en_mongo()
            except:
                pass
            self.archivo_existente = False
        else:
            self.conexion_mongo = False
            if lista_de_grupos is None:
                self.archivo_existente = True
                self.lista_de_grupos = Grupo()  
               
                try:
                    self.cargar_desde_json()
                except:
                    pass
            else:
                self.conexion_mongo = False
                self.archivo_existente = False
                self.lista_de_grupos = lista_de_grupos
    
    def mostrar_menu(self):
        """Método para mostrar el menú de opciones"""
        if self.archivo_existente:
            self.guardar_en_json()
        print("--------------Interfaz de Grupo--------------")
        print("Elige una opción: \n 1. Agregar Grupo \n 2. Ver Grupos \n 3. Borrar Grupo \n 4. Actualizar Grupo \n 5. Salir")
        opcion = input("Inserta el número de la opción que deseas usar:")
        opcion = int(opcion)
        if opcion == 1:
            self.agregar_grupo()
        elif opcion == 2:
            self.mostrar_grupos()
        elif opcion == 3:
            self.eliminar_grupo()
        elif opcion == 4:
            self.actualizar_grupo()
        elif opcion == 5:
            print("Sesión finalizada.")
        else:
            print("Error: Opción no disponible. Verifique que sea solo un número.")
            self.mostrar_menu()
    
    def obtener_datos_del_grupo(self):
        grado = input("Grado:")
        seccion = input("Sección:")
        
        insertar_alumnos = input("¿Deseas agregar alumnos? (1. Sí / 2. No):")
        if insertar_alumnos == "1":
            alumnado = Alumno()  # Crear instancia de Alumno
            interfaz_alumnos = InterfazAlumno(alumnado)  # Interfaz para agregar alumnos
            interfaz_alumnos.mostrar_menu()
            lista_de_alumnos = interfaz_alumnos.lista_de_alumnos
        else:
            lista_de_alumnos = Alumno()  # Sin alumnos
        
        # Crear y retornar el nuevo grupo con los alumnos
        nuevo_grupo = Grupo(grado, seccion)
        for alumno in lista_de_alumnos.lista:
            nuevo_grupo.agregar_alumno(alumno)
        return nuevo_grupo
    
    def agregar_grupo(self):
        """Agregar un nuevo grupo"""
        nuevo_grupo = self.obtener_datos_del_grupo()
        self.lista_de_grupos.agregar_objeto(nuevo_grupo)  
        print("¡Grupo agregado exitosamente!")
        
        datos_grupo = nuevo_grupo.obtener_dict_grupo()  
        if self.conexion_mongo:
            self.guardar_en_mongo(datos_grupo)  
        self.mostrar_menu()
    
    def mostrar_grupos(self):
        """Mostrar los grupos existentes"""
        if not self.lista_de_grupos.lista:
            print("No hay grupos disponibles.")
        else:
            print(self.lista_de_grupos)
        self.mostrar_menu()
    
    def eliminar_grupo(self):
        """Borrar un grupo por su índice"""
        self.mostrar_grupos()
        try:
            indice = int(input("Índice del Grupo que deseas borrar:")) - 1
            if 0 <= indice < len(self.lista_de_grupos.lista):
                self.lista_de_grupos.eliminar_objeto(indice)
                print("¡Grupo eliminado exitosamente!")
                if self.conexion_mongo:
                    self.eliminar_de_mongo()
                    self.guardar_en_mongo()
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        self.mostrar_menu()
    
    def actualizar_grupo(self):
        """Actualizar los detalles de un grupo"""
        self.mostrar_grupos()
        try:
            indice = int(input("Índice del Grupo que deseas actualizar:")) - 1
            if 0 <= indice < len(self.lista_de_grupos.lista):
                grado = input("Nuevo Grado:")
                seccion = input("Nueva Sección:")
                
                modificar_alumnos = input("¿Deseas modificar los alumnos? (1. Sí / 2. No):")
                if modificar_alumnos == "1":
                    grupo_existente = self.lista_de_grupos.lista[indice]
                    interfaz_alumnos = InterfazAlumno(grupo_existente.lista_de_alumnos)
                    interfaz_alumnos.mostrar_menu()
                    lista_de_alumnos_actualizada = interfaz_alumnos.lista_de_alumnos
                else:
                    grupo_existente = self.lista_de_grupos.lista[indice]
                    lista_de_alumnos_actualizada = grupo_existente.lista_de_alumnos
                
                grupo_actualizado = Grupo(grado, seccion)
                for alumno in lista_de_alumnos_actualizada.lista:
                    grupo_actualizado.agregar_alumno(alumno)
                self.lista_de_grupos.editar_objeto(indice, grupo_actualizado)
                print("¡Grupo actualizado exitosamente!")
                
                if self.conexion_mongo:
                    self.eliminar_de_mongo()
                    self.guardar_en_mongo()
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        self.mostrar_menu()

    def guardar_en_json(self, limpiar=False):
        """Guardar la lista de grupos en un archivo JSON"""
        nombre_archivo = "Lista_de_Grupos.json"
        if limpiar:
            grupo_vacio = Grupo()
            grupo_vacio.guardar_en_json(nombre_archivo)
        else:
            self.lista_de_grupos.guardar_en_json(nombre_archivo)
    
    def cargar_desde_json(self, nombre_archivo="Lista_de_Grupos.json"):
        """Cargar grupos desde un archivo JSON"""
        self.lista_de_grupos.cargar_desde_json(nombre_archivo)
    
    def guardar_en_mongo(self, grupo=None):
        """Guardar grupo en MongoDB"""
        conexion = DB("Grupos")
        if grupo is None:
            datos_grupos = self.lista_de_grupos.obtener_dict_grupo()
        else:
            datos_grupos = grupo
        conexion.insertar_documento(datos_grupos)
    
    def eliminar_de_mongo(self):
        """Eliminar todos los documentos de MongoDB"""
        conexion = DB("Grupos")
        conexion.eliminar_todos_los_documentos()
    
    def cargar_desde_mongo(self):
        """Cargar grupos desde MongoDB"""
        conexion = DB("Grupos")
        documentos = conexion.obtener_documentos()
        self.lista_de_grupos.convertir_a_objetos(documentos)
    
    def verificar_conexion_con_mongo(self):
        """Verificar la conexión con MongoDB"""
        conexion = DB("Grupos")
        conexion_activa = conexion.ping()
        return conexion_activa


if __name__ == "__main__":
    interfaz_de_grupo = interfazGrupo()
    interfaz_de_grupo.mostrar_menu()
