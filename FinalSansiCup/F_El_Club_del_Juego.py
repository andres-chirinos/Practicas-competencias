from math import gcd
from functools import reduce



# Función para calcular el mínimo común múltiplo (MCM)
def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

# Función para calcular la probabilidad en fracción irreducible
def calcular_probabilidad(numeradores, denominadores, mod):
    x = reduce(lcm, denominadores)
    y = sum((x // d) * n for n, d in zip(numeradores, denominadores))
    return y % mod

# Lectura de entrada
n, m = map(int, input().split())
numeros_favoritos = list(map(int, input().split()))

# Inicializar numeradores y denominadores
numeradores = [1] * n
denominadores = [1] * n

# Calcular probabilidades
for i in range(n):
    for j in range(1, m + 1):
        if numeros_favoritos[i] % j != 0:
            denominadores[i] *= m
            numeradores[i] *= (m - 1)

# Calcular el inverso multiplicativo modular para cada denominador
inversos_modulares = [pow(d, -1, 10**9 + 9) for d in denominadores]

# Calcular y mostrar las probabilidades finales
probabilidades = [calcular_probabilidad([numeradores[i]], [denominadores[i]], 10**9 + 9) for i in range(n)]

for i, p in enumerate(probabilidades):
    print(p * inversos_modulares[i] % (10**9 + 9))

