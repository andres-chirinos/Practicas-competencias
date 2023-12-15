from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
   g = defaultdict(list)
   for l,r,c in edges:
       g[l].append((c,r))
       g[r].append((c,l))
   q, seen = [(0,f,())], set()
   while q:
       (cost,v1,path) = heappop(q)
       if v1 not in seen:
           seen.add(v1)
           path = (v1, path)
           if v1 == t: return cost
           for c, v2 in g.get(v1, ()):
               if v2 not in seen:
                   heappush(q, (cost+c, v2, path))
   return "-1"

N, M = (int(x) for x in input().split(" "))
graph = [tuple(int(x) for x in input().split(" ")) for _ in range(M)]
for i in range(len(graph)):
    graph2 = graph.copy()
    graph2.pop(i)
    print(dijkstra(graph2, graph[i][0], graph[i][1]))