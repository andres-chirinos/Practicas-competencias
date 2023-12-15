from collections import defaultdict
from heapq import heappop, heappush
 
def dijkstra(edges, f, t, k):
    graph = defaultdict(list)
    for l, r, c, j in edges:
        graph[l].append((c, j, r))
    queue, seen = [(0, 0, f, ())], set()
    while queue:
        costh, costl, v1, path = heappop(queue)
        seen.add(v1)
        path = (v1, path)
        if v1 == t and costl <= k:
            return costh #(, costl, path)
        for ch, cl, v2 in graph.get(v1, ()):
            if v2 not in seen:
                heappush(queue, (costh + ch, costl + cl, v2, path))
    return "-1"
 
edges = []
n, m, k = map(int, input().split())
for i in range(m):
    a, b, h, l = map(int, input().split())
    edges.append((a, b, l, h))
    print(dijkstra(edges, 1, n, k))