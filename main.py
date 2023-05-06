from ManejadorAlumnos import Manejador_Alumno
from ManejadorMaterias import Manejador_Materias
from ClassMenu import Menu

if __name__ == "__main__":
    arreglo = Manejador_Alumno.inicializar()
    manejadorAlumno = Manejador_Alumno(arreglo)

    lista = Manejador_Materias.inicializar()
    manejadorMateria = Manejador_Materias(lista)
    
    Menu(manejadorMateria, manejadorAlumno)
    
 