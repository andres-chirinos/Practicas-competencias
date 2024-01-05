for _ in range(int(input())):
    arr = list(map(int,input().split()))
    for a in set(arr):
        if arr.count(a) == 1:
            print(a)
            break
    