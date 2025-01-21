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
    [202, 202, 202, 0, 0],
    [0, 0, 202, 0, 0],
    [0, 0, 202, 0, 0],
    [0, 0, 202, 0, 0],
    [0, 0, 202, 0, 0],
    [0, 0, 202, 0, 0]
], dtype=np.uint8)


# Función para mostrar la imagen con círculos
def mostrar_imagen_circulos(matriz, titulo):
    filas, columnas = matriz.shape
    x, y = np.meshgrid(range(columnas), range(filas))

    # Aplanar para scatter
    x = x.ravel()
    y = y.ravel()
    colores = matriz.ravel()

    # Crear scatter plot
    plt.scatter(x, -y, c=colores, cmap='gray', s=500, edgecolor='black', vmin=0, vmax=255)
    plt.title(titulo)
    plt.axis('off')
    plt.show()


#  imagen original
mostrar_imagen_circulos(matriz, "Imagen original")

# Solicitar entrada del usuario
x = int(input("Introduzca la fila del nuevo punto de partida: "))
y = int(input("Introduzca la columna del nuevo punto de partida: "))
color_nuevo = int(input("Introduzca el nuevo color (0-255): "))

# flood fill
flood_fill(matriz, x, y, color_nuevo)

# imagen modificada
mostrar_imagen_circulos(matriz, "Imagen modificada")
