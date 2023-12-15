from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(edges, start_node, end_node):
    # Crear un grafo de defaultdict para representar las conexiones entre nodos
    graph = defaultdict(list)
    for left, right, cost in edges:
        graph[left].append((cost, right))
        graph[right].append((cost, left))

    # Inicializar la cola de prioridad con el nodo de inicio y una lista vacía como camino
    priority_queue = [(0, start_node, ())]

    # Conjunto para llevar un registro de los nodos visitados
    visited = set()

    while priority_queue:
        current_cost, current_node, path = heappop(priority_queue)

        # Si ya hemos visitado este nodo, lo omitimos
        if current_node in visited:
            continue

        # Agregar el nodo actual a los visitados y actualizar el camino
        visited.add(current_node)
        path = (current_node, path)

        # Si llegamos al nodo de destino, retornar el costo mínimo
        if current_node == end_node:
            return current_cost

        # Expandir el grafo y agregar los vecinos no visitados a la cola de prioridad
        for cost, neighbor in graph.get(current_node, ()):
            if neighbor not in visited:
                heappush(priority_queue, (current_cost + cost, neighbor, path))

    # Si no se encuentra un camino, retornar "-1"
    return "-1"

# Leer la entrada
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Calcular los caminos mínimos excluyendo un enlace a la vez
for i in range(len(edges)):
    edges_without_i = edges[:i] + edges[i+1:]
    result = dijkstra(edges_without_i, edges[i][0], edges[i][1])
    print(result)
