def fruti(n:str):
  suma_digitos = sum(list(map(int, n)))
  for x in n:
    if (suma_digitos-int(x)) % 3 == 0:
      return True
  return False

s = 0
for _ in range(int(input())):
  n = input()
  if fruti(n):
    s += 1
print(s)