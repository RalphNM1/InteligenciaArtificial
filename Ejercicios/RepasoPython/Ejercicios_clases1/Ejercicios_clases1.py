# Clases base
from datetime import datetime
from Medico import Medico
from Enfermera import Enfermera
from Trabajador import Trabajador

lista_trabajadores = []


# Funciones auxiliares
def introducir_datos_trabajador():
    while True:
        nif = input("Introduzca el NIF del trabajador: ")
        if any(trabajador.nif == nif for trabajador in lista_trabajadores):
            print("El NIF ya existe. Por favor, introduzca otro.")
        else:
            nombre = input("Introduzca el nombre del trabajador: ")
            fecha_nac = input("Introduzca la fecha de nacimiento (formato DD/MM/AAAA): ")
            num_colegiado = input("Introduzca el número de colegiado (opcional, pulse Enter si no aplica): ")
            sexo = input("Introduzca el sexo (M/F): ")
            return nif, nombre, fecha_nac, num_colegiado, sexo


def eliminar_trabajador(lista_trabajadores, nif):
    for trabajador in lista_trabajadores:
        if trabajador.nif == nif:
            lista_trabajadores.remove(trabajador)
            print("Trabajador eliminado.")
            return
    print("No se encontró ningún trabajador con ese NIF.")


# Menú principal
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
            nif, nombre, fecha_nac, num_colegiado, sexo = introducir_datos_trabajador()
            especialidad = input("Introduzca la especialidad del médico: ")
            fecha_comienzo = input("Introduzca la fecha en la que comenzó a ejercer (formato DD/MM/AAAA): ")
            medico_nuevo = Medico(nif, nombre, fecha_nac, num_colegiado, sexo, especialidad, fecha_comienzo)
            lista_trabajadores.append(medico_nuevo)
            print(f"\nEl médico {medico_nuevo.nombre} ha sido añadido correctamente.\n")
        elif tipo_trabajador == 2:
            nif, nombre, fecha_nac, num_colegiado, sexo = introducir_datos_trabajador()
            area = input("Introduzca el área de la enfermera: ")
            personas_acargo = int(input("Introduzca el número de personas a cargo: "))
            enfermera_nueva = Enfermera(nif, nombre, fecha_nac, num_colegiado, sexo, area, personas_acargo)
            lista_trabajadores.append(enfermera_nueva)
            print(f"\nLa enfermera {enfermera_nueva.nombre} ha sido añadida correctamente.\n")

    elif opcion == 2:
        nif = input("Introduzca el NIF del trabajador que desea eliminar: ")
        eliminar_trabajador(lista_trabajadores, nif)

    elif opcion == 3:
        if not lista_trabajadores:
            print("No hay trabajadores registrados.")
        else:
            print("\nTrabajadores\n---------------")
            for trabajador in lista_trabajadores:
                print(f"{trabajador.nombre} con NIF {trabajador.nif}, nacido el {trabajador.fecha_nac}, es un {trabajador.describeme()}.")

    elif opcion == 4:
        nif_buscar = input("Introduzca el NIF del trabajador que desea ver: ")
        for trabajador in lista_trabajadores:
            if trabajador.nif == nif_buscar:
                print(f"\nDetalle del trabajador:\nNIF: {trabajador.nif}\nNombre: {trabajador.nombre}\nFecha de nacimiento: {trabajador.fecha_nac}")
                if isinstance(trabajador, Medico):
                    print(f"Especialidad: {trabajador.especialidad}\nFecha de comienzo: {trabajador.fecha_comienzo}")
                elif isinstance(trabajador, Enfermera):
                    print(f"Área: {trabajador.area}\nPersonas a cargo: {trabajador.personas_acargo}")
                break
        else:
            print("No se encontró ningún trabajador con ese NIF.")

    elif opcion == 5:
        nif_buscar = input("Introduzca el NIF del médico: ")
        for trabajador in lista_trabajadores:
            if isinstance(trabajador, Medico) and trabajador.nif == nif_buscar:
                print(f"{trabajador.nombre} ha trabajado {Medico.mostrar_años_trabajados(trabajador.fecha_comienzo)} años.")
                break
        else:
            print("No se encontró un médico con ese NIF.")

    elif opcion == 6:
        nif_buscar = input("Introduzca el NIF de la enfermera: ")
        for trabajador in lista_trabajadores:
            if isinstance(trabajador, Enfermera) and trabajador.nif == nif_buscar:
                trabajador.mostrar_personas_acargo()
                break
        else:
            print("No se encontró una enfermera con ese NIF.")

    elif opcion == 7:
        nif_buscar = input("Introduzca el NIF de la enfermera: ")
        cantidad = int(input("¿Cuántas personas quiere añadir a cargo? "))
        for trabajador in lista_trabajadores:
            if isinstance(trabajador, Enfermera) and trabajador.nif == nif_buscar:
                trabajador.añadir_personas_acargo(cantidad)
                break
        else:
            print("No se encontró una enfermera con ese NIF.")

    elif opcion == 8:
        nif_buscar = input("Introduzca el NIF de la enfermera: ")
        cantidad = int(input("¿Cuántas personas quiere reducir a cargo? "))
        for trabajador in lista_trabajadores:
            if isinstance(trabajador, Enfermera) and trabajador.nif == nif_buscar:
                trabajador.reducir_personas_acargo(cantidad)
                break
        else:
            print("No se encontró una enfermera con ese NIF.")

    elif opcion == 9:
        print("¡Adiós!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
