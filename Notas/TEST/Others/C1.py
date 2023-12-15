from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(aristas, inicio, fin, k):
    grafo = defaultdict(list)
    for a, b, h, l in aristas:
        grafo[a].append((b, h, l))
    cola, visitados = [(0, 0, inicio, ())], set()
    while cola:
        costo_h, costo_l, actual, camino = heappop(cola)
        if actual not in visitados and costo_l <= k:
            visitados.add(actual)
            camino = (actual, camino)
            if actual == fin:
                return costo_h
            for costo_h_i, costo_l_i, v2 in grafo.get(actual, ()):
                if v2 not in visitados and (costo_l + costo_l_i) <= k:
                    heappush(cola, (costo_h + costo_h_i, costo_l + costo_l_i, v2, camino))
    return "-1"

aristas = []
n, m, k = map(int, input().split())
for i in range(m):
    a, b, h, l = map(int, input().split())
    aristas.append((a, b, h, l))
print(dijkstra(aristas, 1, n, k))
