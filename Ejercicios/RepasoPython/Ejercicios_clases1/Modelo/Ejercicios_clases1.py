

"""
Gestión de Trabajadores de un Hospital
======================================

Este módulo proporciona funcionalidades para la gestión de trabajadores 
en un hospital, incluyendo médicos y enfermeras.

Clases Base
-----------
Las clases base utilizadas en este programa se encuentran en el módulo `Modelo`.
- `Medico`
- `Enfermera`
- `Trabajador`

Funciones Principales
---------------------
"""
# No consigo que me pille Ejercicios_clase1 y el resto de clases desde fuera de otra carpeta, por eso la distribucion tan rara
from datetime import datetime
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Medico import Medico
from Enfermera import Enfermera
from Trabajador import Trabajador

# Lista de trabajadores
lista_trabajadores = []

def introducir_datos_trabajador():
    """
    Solicita y valida la información básica de un trabajador.

    :return: Tupla con los datos del trabajador: NIF, nombre, fecha de nacimiento,
             número de colegiado (opcional) y sexo.
    """
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
    """
    Elimina un trabajador de la lista dado su NIF.

    :param lista_trabajadores: Lista actual de trabajadores.
    :param nif: NIF del trabajador a eliminar.
    """
    for trabajador in lista_trabajadores:
        if trabajador.nif == nif:
            lista_trabajadores.remove(trabajador)
            print("Trabajador eliminado.")
            return
    print("No se encontró ningún trabajador con ese NIF.")

def guardar_datos_csv(nombre_archivo):
    """
    Guarda los datos de los trabajadores en un archivo CSV.

    :param nombre_archivo: Nombre del archivo donde se guardarán los datos.
    """

    trabajadores_df = pd.DataFrame( {"Name": ["Alice", "Bob"], "Age": [25, 30]})
    print(trabajadores_df)
    
    for trabajador in lista_trabajadores:
            if isinstance(trabajador, Medico): 
                data = {"Puesto":["Medico"],"NIF": [trabajador.nif], "nombre": [trabajador.nombre], "fecha_nac" : [trabajador.fecha_nac], 
                        "num_colegiado": trabajador.num_colegiado,"sexo": trabajador.sexo, 
                        "especialidad": trabajador.especialidad, "fecha_comienzo":trabajador.fecha_comienzo}
                
      
                trabajadores_df.loc[len(trabajadores_df)] =  data
             

            elif isinstance(trabajador, Enfermera):
                data = {"Puesto":["Enfermera"] ,"NIF": [trabajador.nif], "nombre": [trabajador.nombre], "fecha_nac" : [trabajador.fecha_nac], 
                        "num_colegiado": trabajador.num_colegiado,"sexo": trabajador.sexo, 
                        "area": trabajador.area, "personas_acargo":trabajador.personas_acargo}
                trabajadores_df.loc[len(trabajadores_df)] =  data

    trabajadores_df.to_csv(nombre_archivo, sep=',')

    print(f"Datos guardados en {nombre_archivo}.")



"""
    with open(nombre_archivo, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        for trabajador in lista_trabajadores:
            if isinstance(trabajador, Medico):
                escritor.writerow(["Medico", trabajador.nif, trabajador.nombre, trabajador.fecha_nac, 
                                   trabajador.num_colegiado, trabajador.sexo, trabajador.especialidad, 
                                   trabajador.fecha_comienzo])
            elif isinstance(trabajador, Enfermera):
                escritor.writerow(["Enfermera", trabajador.nif, trabajador.nombre, trabajador.fecha_nac, 
                                   trabajador.num_colegiado, trabajador.sexo, trabajador.area, 
                                   trabajador.personas_acargo])
    print(f"Datos guardados en {nombre_archivo}.")
"""
    

def cargar_datos_csv(nombre_archivo):
    """
    Carga datos de trabajadores desde un archivo CSV.

    :param nombre_archivo: Nombre del archivo desde el que se cargarán los datos.
    """
    global lista_trabajadores
    lista_trabajadores = []
    try:
        with open(nombre_archivo, mode='r') as archivo:
            lector = csv.reader(archivo)
            for linea in lector:
                tipo = linea[0]
                if tipo == "Medico":
                    _, nif, nombre, fecha_nac, num_colegiado, sexo, especialidad, fecha_comienzo = linea
                    medico = Medico(nif, nombre, fecha_nac, num_colegiado, sexo, especialidad, fecha_comienzo)
                    lista_trabajadores.append(medico)
                elif tipo == "Enfermera":
                    _, nif, nombre, fecha_nac, num_colegiado, sexo, area, personas_acargo = linea
                    enfermera = Enfermera(nif, nombre, fecha_nac, num_colegiado, sexo, area, int(personas_acargo))
                    lista_trabajadores.append(enfermera)
        print(f"Datos cargados desde {nombre_archivo}.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

# Aquí sigue el menú principal y las demás funcionalidades.


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
                       "9. Guardar datos en .csv\n"
                       "10. Cargar datos de .csv\n"
                       "11. Salir\n"))
    
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
        nombre_archivo = input("Introduzca el nombre del archivo para guardar los datos (con extensión .csv): ")
        
        guardar_datos_csv(nombre_archivo)

     
    elif opcion == 10:
        nombre_archivo = input("Introduzca el nombre del archivo para cargar los datos (con extensión .csv): ")
        cargar_datos_csv(nombre_archivo)

        hospital_df = pd.read_csv(nombre_archivo)

        print(hospital_df)

    elif opcion == 11:
        print("¡Adiós!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")



