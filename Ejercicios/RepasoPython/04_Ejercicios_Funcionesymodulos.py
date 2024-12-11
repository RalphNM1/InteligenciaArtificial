
import Ejercicios_03_Funcionesymodulos1 as tres
import Ejercicios_02_Funcionesymodulos1 as dos

exit = False
while exit != True:
    opcion = int(input(
        "\n---------MENÚ---------\n1. Calcular la secuencia de Fibonacci hasta un número\n2. Convertir temperatura de ºC ºF\n3. Salir\n"))

    if (opcion == 1):
        tres.inicio2()
    elif (opcion == 2):
        dos.inicio2()

    elif (opcion == 3):
        exit = True
    else:
        print("Opción incorrecta")

"""
### Crea ahora un archivo Python  donde importes los ejercicios 2 y 3 como módulos. 
Ejecuta el programa solo con los imports.

Responde: ¿Se ha ejecutado algo?
    No.

"""
