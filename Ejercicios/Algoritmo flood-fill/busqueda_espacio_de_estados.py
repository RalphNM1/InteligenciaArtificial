import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 


def flood_fill(matriz, x, y, color_nuevo, color_original=None):
    filas, columnas = matriz.shape
    if color_original is None:
        color_original = matriz[x, y]

    # Si el punto no es del color original o ya tiene el nuevo color
    
    if x < 0 or x >= filas or y < 0 or y >= columnas or matriz[x, y] != color_original or matriz[x, y] == color_nuevo:
        return

    # Cambiar el color del punto actual

    matriz[x, y] = color_nuevo

    # Llamar recursivamente en las 4 direcciones

    flood_fill(matriz, x+1, y, color_nuevo, color_original)
    flood_fill(matriz, x-1, y, color_nuevo, color_original)
    flood_fill(matriz, x, y+1, color_nuevo, color_original)
    flood_fill(matriz, x, y-1, color_nuevo, color_original)


# Matriz inicial

matriz = np.array([
    [0,0,0,0,0],
    [255,255,255,0,0],
    [0,0,255,0,0],
    [0,0,255,0,0],
    [0,0,255,0,0],
    [0,0,255,0,0],
    [0,0,255,0,0]
])

# Imagen origina
# l
y,x = matriz.shape
x, y = np.meshgrid(range(x), range(y))

colores = matriz.flatten()

colores = colores / 255

scatter = plt.scatter(x, -y, c=colores, s=500, cmap='gray', edgecolors='black')
plt.title("Imagen original")
plt.axis('off') 
plt.show()

# Aplicar flood fill

x = int(input("Introduzca la fila del nuevo punto de partida: "))
y = int(input("Introduzca la columna del nuevo punto de partida: "))

color_nuevo = int(input("Introduzca el nuevo color(0-255): "))

flood_fill(matriz, x, y, color_nuevo)

# Imagen modificada

y,x = matriz.shape
x, y = np.meshgrid(range(x), range(y))

colores = matriz.flatten()

colores = colores / 255

scatter = plt.scatter(x, -y, c=colores, s=500, cmap='gray', edgecolors='black')
plt.title("Imagen modificada")
plt.axis('off') 
plt.show()

