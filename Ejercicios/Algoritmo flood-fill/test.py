import matplotlib.pyplot as plt
import numpy as np

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
    [0, 0, 0, 0, 0],
    [100, 100, 100, 0, 0],
    [0, 0, 100, 0, 0],
    [0, 0, 100, 0, 0],
    [0, 0, 100, 0, 0],
    [0, 0, 100, 0, 0],
    [0, 0, 100, 0, 0]
])

def mostrar_con_scatter(matriz, titulo):
    filas, columnas = matriz.shape
    x, y = np.meshgrid(range(columnas), range(filas))  
    colores = matriz.flatten() / 255 
    
    plt.figure(figsize=(6, 6))
    plt.scatter(x.flatten(), -y.flatten(), c=colores, s=500, cmap='gray', edgecolors='black')  # Dibujar círculos
    plt.title(titulo)
    plt.axis('off')  # Quitar ejes
    plt.show()

# Mostrar la imagen original
mostrar_con_scatter(matriz, "Imagen original")

# Aplicar flood fill
x = int(input("Introduzca la fila del nuevo punto de partida: "))
y = int(input("Introduzca la columna del nuevo punto de partida: "))
color_nuevo = int(input("Introduzca el nuevo color (0-255): "))

flood_fill(matriz, x, y, color_nuevo)

# Mostrar la imagen modificada
mostrar_con_scatter(matriz, "Imagen modificada")


