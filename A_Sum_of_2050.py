for _ in range(int(input())):
    n = int(input())
    r = -1
    if n%2050==0:
        r = sum([int(i) for i in str(n//2050)])
    print(r)