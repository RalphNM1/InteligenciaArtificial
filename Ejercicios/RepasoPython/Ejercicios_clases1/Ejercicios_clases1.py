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
def añadir_trabajador(self,Trabajador,lista_trabajadores = []):
    lista_trabajadores.append(Trabajador)

def introducir_datos_trabajador():

    nif = str(input("Introduzca el NIF del trabajador: "))
    nombre = str(input("Introduzca el nombre del trabajador: "))


    return nif,nombre


lista_trabajadores = []
while True:
    opcion = int(input("Gestión de los trabajadores del hospital\n1. Añadir trabajador\n2. Borrar trabajador\n3. Mostrar lista de trabajadores\n4. Mostrar detalle de un trabajador\n5. Mostrar número de años trabajados de un médico\n6. Mostrar número de personas a cargo de una enfermera\n7. Añadir personas a cargo de una enfermera\n8. Reducir personas a cargo de una enfermera\n9.Salir\n"))

    if(opcion == 1):
        tipo_trabajador = int(input("Quiere introducir un medico(1) o una enfermera(2): "))

        if(tipo_trabajador == 1):
            print("medico")
        elseif(tipo_trabajador == 2):
            print("enfermera")

    introducir_datos_trabajador()        
        
        
    if(opcion == 2):
        print()
    if(opcion == 3):
        print()
    if(opcion == 4):
        print()
    if(opcion == 5):
        print()
    if(opcion == 6):
        print()
    if(opcion == 7):
        print()
    if(opcion == 8):
        print()
    if(opcion == 9):
        break