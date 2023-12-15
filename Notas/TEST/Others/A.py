import math
x, y = map(int, input().split())
result = x * math.log10(2) + y * math.log10(5)
digits = int(result) + 1

print(digits)