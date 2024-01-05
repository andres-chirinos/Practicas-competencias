for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = sorted(map(int, input().split()))
    result = 'S'
    for i in range(1, n):
        if arr[i] - arr[i-1] > k:
            result = 'F'
            break
    print(result)
