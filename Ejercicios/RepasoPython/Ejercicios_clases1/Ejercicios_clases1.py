"""
Ejercicio Clases 1
Gestión de un hospital
Se ha de realizar una aplicación para la gestión de los trabajadores de un hospital, en
concreto de dos tipos: enfermeras y médicos
Se almacenan los siguientes datos de cada Trabajador:
● NIF
● Nombre
● Fecha de nacimiento
● Número de colegiado (opcional)
● Sexo
Y como información adicional:
● En el caso de un Médico se indica la especialidad y la fecha en la que comenzó a
ejercer.
● Si se trata de una Enfermera tanto el área en el que trabaja como el número de
personas a su cargo.
Se podrá añadir, borrar y modificar datos de los trabajadores así como obtener listados de
los mismos.
El menú principal tendrá las siguientes opciones:
Gestión de los trabajadores del hospital
1. Añadir trabajador
2. Borrar trabajador
3. Mostrar lista de trabajadores
4. Mostrar detalle de un trabajador
5. Mostrar número de años trabajados de un médico
6. Mostrar número de personas a cargo de una enfermera
7. Añadir personas a cargo de una enfermera
8. Reducir personas a cargo de una enfermera
9.Salir
Realizar todo el control relativo a la entrada de datos. Implementar el ejercicio con clases y
listas.
"""

from Medico import *
from Enfermera import *
lista_trabajadores = []

def añadir_trabajador(self,Trabajador,lista_trabajadores = []):
    lista_trabajadores.append(Trabajador)


def eliminar_trabajador(lista_trabajadores, nif):
    for trabajador in lista_trabajadores:
        if trabajador.nif == nif:
            lista_trabajadores.remove(trabajador)
            print("Trabajador eliminado.")
            break



def introducir_datos_trabajador(lista_trabajadores):
    while True:
        nif = str(input("Introduzca el NIF del trabajador: "))

        # Verifica si el NIF ya existe
        if any(trabajador.nif == nif for trabajador in lista_trabajadores):
            print("El NIF ya existe. Por favor, introduzca otro.")
        else:
            nombre = str(input("Introduzca el nombre del trabajador: "))
            fecha_nac = str(input("Introduzca la fecha de nacimiento (formato DD/MM/AAAA): "))
            num_colegiado = int(input("Introduzca el número de colegiado: "))
            sexo = str(input("Introduzca el sexo (M/F): "))

            return nif, nombre, fecha_nac, num_colegiado, sexo

while True:
    opcion = int(input("\nGestión de los trabajadores del hospital\n"
                       "1. Añadir trabajador\n"
                       "2. Borrar trabajador\n"
                       "3. Mostrar lista de trabajadores\n"
                       "4. Mostrar detalle de un trabajador\n"
                       "5. Mostrar número de años trabajados de un médico\n"
                       "6. Mostrar número de personas a cargo de una enfermera\n"
                       "7. Añadir personas a cargo de una enfermera\n"
                       "8. Reducir personas a cargo de una enfermera\n"
                       "9. Salir\n"))
    
    if opcion == 1:
        tipo_trabajador = int(input("¿Quiere introducir un médico (1) o una enfermera (2)? "))

        if tipo_trabajador == 1:
            nif, nombre, fecha_nac, num_colegiado, sexo = introducir_datos_trabajador(lista_trabajadores)

            especialidad = str(input("Introduzca la especialidad del médico: "))
            fecha_ejer = str(input("Introduzca la fecha en la que comenzó a ejercer (formato DD/MM/AAAA): "))

            medico_nuevo = Medico(nif, nombre, fecha_nac, num_colegiado, sexo, especialidad, fecha_ejer)

            lista_trabajadores.append(medico_nuevo)
            print(f"\nEl médico {medico_nuevo.nombre} ha sido añadido correctamente.\n")
        elif tipo_trabajador == 2:
            nif, nombre, fecha_nac, num_colegiado, sexo = introducir_datos_trabajador(lista_trabajadores)
            area = str(input("Introduzca el area de la enfermer@: "))
            
            personas_acargo = int(input("Introduzca el número de personas a cargo"))

            enfermera_nueva = Enfermera(nif, nombre, fecha_nac, num_colegiado, sexo,area,personas_acargo)

            lista_trabajadores.append(enfermera_nueva)


    if(opcion == 2):
 
        nif = str(input("Introduzca el NIF del trabajador que desea eliminar: "))
        if any(trabajador.nif == nif for trabajador in lista_trabajadores):
            eliminar_trabajador(lista_trabajadores,nif)
        else:
            print("El trabajador no existe.")

    
    if(opcion == 3):
        if not lista_trabajadores:
            print("\nTrabajadores\n---------------")
            print("No hay trabajadores.")
        else:
            print("\nTrabajadores\n---------------")
            for trabajador in lista_trabajadores:
                print(f"{trabajador.nombre} con NIF {trabajador.nif}, nacido el {trabajador.fecha_nac} y es un {trabajador.describeme()}" )


    if(opcion == 4):
       nif_buscar =  input("Introduzca el dni del trabajador del que necesita información")


    if(opcion == 5):
     print(Medico.mostrar_años_trabajados("05/11/2004"))   
    if(opcion == 6):
        Enfermera.mostrar_personas_acargo("enfermera")
    if(opcion == 7):
        Enfermera.añadir_personas_acargo("enfermera",4)
    if(opcion == 8):
        Enfermera.reducir_personas_acargo("enfermera",4)
    if(opcion == 9):
        break