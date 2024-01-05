for _ in range(int(input())):
  s=0
  inc=1
  b=3
  for i in range(int(input())):
    s+=inc*((-1)**i)
    inc+=b
    b+=2
  print(s)