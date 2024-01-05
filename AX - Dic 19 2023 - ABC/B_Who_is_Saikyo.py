N,M = map(int, input().split())
dicts = {i:set() for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int, input().split())
    dicts[a].add(b)

#encontrar el nodo con mas hijos y contarlos (si hay mas de uno, no es saikyo)
max_hijos = 0
max_hijos_nodo = 0
for i in range(1,N+1):
    if len(dicts[i]) > max_hijos:
        max_hijos = len(dicts[i])
        max_hijos_nodo = i
if max_hijos > 1:
    print(-1)
else:
    #encontrar el nodo con mas padres y contarlos (si hay mas de uno, no es saikyo)
    max_padres = 0
    max_padres_nodo = 0
    for i in range(1,N+1):
        cont = 0
        for j in range(1,N+1):
            if i in dicts[j]:
                cont += 1
        if cont > max_padres:
            max_padres = cont
            max_padres_nodo = i
    if max_padres > 1:
        print(-1)
    else:
        print(max_hijos_nodo)