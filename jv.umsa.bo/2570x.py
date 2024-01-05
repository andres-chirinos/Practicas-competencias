def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)

def esprimo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

fibol = {fibo(i) for i in range(0, 31)}

while True:
  a,b = map(int, input().split(" "))
  if a == 0 and b == 0:
    break
  if (all(int(ai) in fibol for ai in str(a)) and esprimo(a)) and (all(int(bi) in fibol for bi in str(b)) and esprimo(b)):
    print("SI")
  else:
    print("NO")