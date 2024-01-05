def generararea(Ai, Bi, Ci, Di):
    puntos_area = set()
    for i in range(min(Ai, Bi),max(Ai, Bi)):
        for j in range(min(Ci, Di),max(Ci, Di)):
            puntos_area.add((i, j))
    return puntos_area

N = int(input())
area_total = set()
for _ in range(N):
    Ai,Bi,Ci,Di = map(int, input().split())
    area_total = area_total.union(generararea(Ai, Bi, Ci, Di))
print(len(area_total))