def buscar():
  a=V[0]+V[1]
  b=0
  for i in range(1,n):
    r = V[i]+V[i-1]
    if (not (r==a or r==b) and b==0):
      b=r
    elif (r!=a and b!=0):
      return False
  return True

for _ in range(int(input())):
  n = int(input())
  V = [int(x) for x in input().split()]
  if buscar():
    print("yes")
  else:
    print("no")
