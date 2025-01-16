from collections import deque

# Laberinto representado como una matriz
# 0 = espacio libre, 1 = muro
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

# Dirección de movimiento (arriba, abajo, izquierda, derecha)
direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def es_valido(x, y, laberinto, visitado):
    """Verifica si la posición (x, y) es válida para moverse"""
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 0 and not visitado[x][y]

def bfs(laberinto, inicio, fin):
    """Implementación de BFS para encontrar el camino más corto en el laberinto"""
    # Crear una matriz de visitados para marcar los nodos visitados
    visitado = [[False for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]
    
    # Cola para la BFS, almacenará las posiciones y el camino
    cola = deque([(inicio, [inicio])])
    visitado[inicio[0]][inicio[1]] = True

    while cola:
        (x, y), camino = cola.popleft()

        # Si llegamos al destino, devolvemos el camino
        if (x, y) == fin:
            return camino

        # Explorar las 4 direcciones posibles
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if es_valido(nx, ny, laberinto, visitado):
                visitado[nx][ny] = True
                cola.append(((nx, ny), camino + [(nx, ny)]))

    # Si no hay camino, retornamos None
    return None

# Definir el punto de inicio y el punto de destino
inicio = (0, 0)  # (Fila, Columna)
fin = (4, 4)     # (Fila, Columna)

# Ejecutar la búsqueda en anchura (BFS)
camino = bfs(laberinto, inicio, fin)

if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino.")