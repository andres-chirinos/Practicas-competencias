while True:
  a,b,c = (int(x) for x in input().split(" "))
  if a == 0 and b == 0 and c == 0:
    break
  d = 0
  for i in range(0, a, b):
    if i % c ==0:
      d=d+1
  print(d)