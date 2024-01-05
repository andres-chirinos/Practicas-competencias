"""N, S = map(int, input().split())
Nv = [tuple(map(int, input().split())) for _ in range(N)]
Dt = 0
Ct = 0
t = max(Nv)[1]+1
for li, ri, ci in reversed(Nv):
  du = abs(li-t)
  if du*S-ci>0:
    t-=du
    Dt+=du
    Ct+=ci
print(Dt*S-Ct, Dt,Ct)"""
N, S = map(int, input().split())
trabajos = [tuple(map(int, input().split())) for _ in range(N)]
trabajos.sort(key=lambda x: (abs(x[1]-x[0])+1)*S-x[2], reverse = True)
diasocupados = set()
for li, ri, ci in trabajos:
  if not any(x>=li for x in diasocupados) and abs((li-ri)+1)*S-ci>0:
    print(li,ri,ci)
    diasocupados.add(li)
print(diasocupados)
