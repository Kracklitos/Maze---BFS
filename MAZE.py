from collections import deque  # Importar la clase deque de la librería collections

def initialize_visited(rows, cols):
    # Inicializar una matriz de visitados con False
    return [[False for _ in range(cols)] for _ in range(rows)]

def find_path_bfs(maze, start, goal):
    num_rows, num_cols = len(maze), len(maze[0])  # Obtener las dimensiones del laberinto
    visited = initialize_visited(num_rows, num_cols)  # Inicializar matriz de nodos visitados
    queue = deque([(start, [start])])  # Inicializar cola con el nodo inicial y su camino

    while queue:  # Mientras la cola no esté vacía
        (row, col), path = queue.popleft()  # Obtener el nodo actual y su camino desde la cola
        visited[row][col] = True  # Marcar el nodo actual como visitado

        if (row, col) == goal:  # Si se llega al nodo objetivo
            return path  # Devolver el camino hasta el objetivo

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Definir las direcciones posibles

        for d_row, d_col in directions:  # Iterar sobre las direcciones posibles
            new_row, new_col = row + d_row, col + d_col  # Calcular las coordenadas del nodo vecino
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and not visited[new_row][new_col] and maze[new_row][new_col] == 0:
                # Verificar si el nodo vecino es válido y no ha sido visitado
                new_path = path + [(new_row, new_col)]  # Actualizar el camino con el nodo vecino
                queue.append(((new_row, new_col), new_path))  # Agregar el nodo vecino a la cola con su nuevo camino
                visited[new_row][new_col] = True  # Marcar el nodo vecino como visitado

    return None  # Si no se encuentra un camino válido, devolver None

# Ejemplo de uso
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start_node = (0, 0)  # Nodo inicial
goal_node = (4, 4)   # Nodo objetivo

path_found = find_path_bfs(maze, start_node, goal_node)  # Encontrar el camino utilizando BFS
print(path_found)  # Imprimir el camino encontrado
