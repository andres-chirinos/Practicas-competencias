from collections import defaultdict
from heapq import *

N, M = map(int, input().split(" "))
edges = defaultdict(list)
for _ in range(N):
  a,b,t = map(int, input().split(" "))
  edges[a].append((b,t))
  q, seen = [(0,f)]


import heapq

def dijkstra(grafo, inicio):
    distancia = {vertice: float('infinity') for vertice in grafo}
    distancia[inicio] = 0

    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        dist_actual, vertice_actual = heapq.heappop(cola_prioridad)

        if dist_actual != distancia[vertice_actual]:
            continue

        for vecino, peso in grafo[vertice_actual].items():
            dist_vecino = distancia[vertice_actual] + peso

            if dist_vecino < distancia[vecino]:
                distancia[vecino] = dist_vecino
                heapq.heappush(cola_prioridad, (dist_vecino, vecino))

    return distancia
    
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(grafo, 'A'))