from ManejadorMaterias import Manejador_Materias
from ManejadorAlumnos import Manejador_Alumno

class Menu:
    __manejadorMateria:"Manejador_Materias"
    __manejadorAlumno:"Manejador_Alumno"
    __switcher:dict

    def __init__(self, manejador1:"Manejador_Materias", manejador2:"Manejador_Alumno")->None:
        self.__manejadorMateria=manejador1
        self.__manejadorAlumno=manejador2
        self.__switcher={
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3
        }
        self.Opciones()

    def Opciones(self)->None:
        self.__mostrarmenu()
        opcion=int(input("\nIngrese la opcion: "))
        while opcion!=0:
            if opcion in self.__switcher:
                self.__switcher[opcion]()
            else: print("Opcion incorrecta. ")
            opcion=int(input("\nIngrese la opcion: "))

    def __mostrarmenu(self)->None:
        print("--------Opciones--------")
        print("1: Buscar promedios. ")
        print("2: Informar estudiantes promocionales. ")
        print("3: Lista ordenada de alumnos. ")
        print("0: Salir. ")

    def opcion1(self)->None:
        dni = input("Ingrese el DNI del alumno: ")
        self.__manejadorMateria.mostrar_promedio(dni)

    def opcion2(self)->None:
        lista = self.buscar_alumno(input("Ingrese el Nombre de la materia: "))
        if lista:
            print("    DNI      Apellido y nombre          Fecha     Nota  Año que cursa ")
            print("--------- -------------------------  ----------  -----  ------------ ")
            for alumno in lista:
                print(f"{alumno[0]:<10} {alumno[1]:<25} {alumno[2]:<14} {alumno[3]:.2f}  {alumno[4]}")
        else: print("No hay ningun alumno promocional. ")

    def buscar_alumno(self, materia:str)->list[tuple[str, str, str, float, int]]:
        promocionales=[]
        lista1 = self.__manejadorMateria.busca_promocional(materia)
        lista2 = []
        for catedra in lista1:
            lista2.append(catedra.get_Dni())
        for dni in lista2:
            seleccionado = self.__manejadorAlumno.busca_alumno(dni)
            for lista1 in lista1:
                dni=lista1.get_Dni()
                nombre = seleccionado.get_Nombrecompleto()
                fecha = lista1.get_fecha()
                nota = float(lista1.get_nota())
                ano = int(seleccionado.get_ano())
                promocionales.append((dni, nombre, fecha, nota, ano))
        return promocionales

    def opcion3(self):
        lista=self.__manejadorAlumno.ordenar()
        print("Lista ordenada: ")
        for elemento in lista:
            print(elemento)
        
    
        

    