def is_palin(n):
    return str(n) == str(n)[::-1]

def change_base(n, b):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b
    return "".join(digits[::-1])

n=int(input())
arr = list()
for i in range(2,n+1):
    if is_palin(change_base(n,i)):
        arr.append(i)
if not arr:
    print("*")
else:
    print(*arr)