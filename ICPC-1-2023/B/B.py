def resuelve_problema_baraja_barajada(N, permutacion):
    matriz = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                matriz[i, j] = 0
            else:
                matriz[i, j] = min(matriz[i - 1, j], matriz[i, j - 1]) + 1
    return matriz[N, N]


if __name__ == "__main__":
    N = int(input())
    permutacion = list(map(int, input().split()))
    print(resuelve_problema_baraja_barajada(N, permutacion))
