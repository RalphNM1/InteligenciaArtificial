

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
            num_colegiado = input("Introduzca el número de colegiado (opcional, pulse Enter para omitirlo): ")
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

    trabajadores_data = []

    for trabajador in lista_trabajadores:
        if isinstance(trabajador, Medico):
            trabajadores_data.append({
                "Puesto": "Medico",
                "NIF": trabajador.nif,
                "Nombre": trabajador.nombre,
                "Fecha de Nacimiento": trabajador.fecha_nac,
                "Número de Colegiado": trabajador.num_colegiado,
                "Sexo": trabajador.sexo,
                "Especialidad": trabajador.especialidad,
                "Fecha de Comienzo": trabajador.fecha_comienzo,
            })
        elif isinstance(trabajador, Enfermera):
            trabajadores_data.append({
                "Puesto": "Enfermera",
                "NIF": trabajador.nif,
                "Nombre": trabajador.nombre,
                "Fecha de Nacimiento": trabajador.fecha_nac,
                "Número de Colegiado": trabajador.num_colegiado,
                "Sexo": trabajador.sexo,
                "Área": trabajador.area,
                "Personas a Cargo": trabajador.personas_acargo,
            })


    df = pd.DataFrame(trabajadores_data)
    print(df)
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos guardados en {nombre_archivo}.")
    
def lista_a_df():
    trabajadores_data = []

    for trabajador in lista_trabajadores:
        if isinstance(trabajador, Medico):
            trabajadores_data.append({
                "Puesto": "Medico",
                "NIF": trabajador.nif,
                "Nombre": trabajador.nombre,
                "Fecha de Nacimiento": trabajador.fecha_nac,
                "Número de Colegiado": trabajador.num_colegiado,
                "Sexo": trabajador.sexo,
                "Especialidad": trabajador.especialidad,
                "Fecha de Comienzo": trabajador.fecha_comienzo,
            })
        elif isinstance(trabajador, Enfermera):
            trabajadores_data.append({
                "Puesto": "Enfermera",
                "NIF": trabajador.nif,
                "Nombre": trabajador.nombre,
                "Fecha de Nacimiento": trabajador.fecha_nac,
                "Número de Colegiado": trabajador.num_colegiado,
                "Sexo": trabajador.sexo,
                "Área": trabajador.area,
                "Personas a Cargo": trabajador.personas_acargo,
            })


    df = pd.DataFrame(trabajadores_data)
    return df

def cargar_datos_csv(nombre_archivo):
    """
    Carga datos de trabajadores desde un archivo CSV.

    :param nombre_archivo: Nombre del archivo desde el que se cargarán los datos.
    """
    df = pd.read_csv(nombre_archivo, skipinitialspace=True)

    for _, row in df.iterrows():
        if row["Puesto"] == "Medico":
            medico = Medico(
                nif=row["NIF"],
                nombre=row["Nombre"],
                fecha_nac=row["Fecha de Nacimiento"],
                num_colegiado=row["Número de Colegiado"],
                sexo=row["Sexo"],
                especialidad=row["Especialidad"],
                fecha_comienzo=row["Fecha de Comienzo"]
            )
            lista_trabajadores.append(medico)
        elif row["Puesto"] == "Enfermera":
            enfermera = Enfermera(
                nif=row["NIF"],
                nombre=row["Nombre"],
                fecha_nac=row["Fecha de Nacimiento"],
                num_colegiado=row["Número de Colegiado"],
                sexo=row["Sexo"],
                area=row["Área"],
                personas_acargo=int(row["Personas a Cargo"])
            )
            lista_trabajadores.append(enfermera)


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
                       "11. GRAFOS \n"
                       "12. Salir\n"))
    
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
        df = cargar_datos_csv(nombre_archivo)

    elif opcion == 11:
        print("GRAFOS: ")
        hospital_df = lista_a_df()

        #print(duckdb.query("SELECT COUNT(Área) FROM hospital_df where Área like 'Urgencias'").df()) # returns a result dataframe


        # Filtrar el DataFrame excluyendo a los médicos
        hospital_df_enfermeras = hospital_df[hospital_df["Puesto"] != "Medico"]

        #print(hospital_df_enfermeras)

                # Gráfico de barras para las personas a cargo de las enfermeras
        hospital_df_enfermeras = hospital_df[hospital_df["Puesto"] == "Enfermera"]

        plt.bar(hospital_df_enfermeras["Nombre"], hospital_df_enfermeras["Personas a Cargo"])
        plt.xlabel('Nombre')
        plt.ylabel('Personas a Cargo')
        plt.title('Personas a cargo por enfermera')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()


                # Gráfico de distribución por área
        sns.countplot(data=hospital_df_enfermeras, x="Área", palette="viridis", order=hospital_df["Área"].value_counts().index)
        plt.xlabel("Área")
        plt.ylabel("Número de personas")
        plt.title("Distribución de personal por área")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()



        """fig = px.bar(hospital_df, x="Área", color="Puesto", title="Distribución del personal por área y puesto")
fig.show()"""

    elif opcion == 12:
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")



