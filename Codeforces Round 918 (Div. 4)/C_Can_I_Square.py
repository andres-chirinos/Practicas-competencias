def f(n):
    if n==0:
        return 1
    return f(n-1)+1+2*n

for _ in range(int(input())):
    N = int(input())
    a = sum(list(map(int,input().split())))
    i = 1
    sw=False
    while a >= f(i):
        if a==f(i):
            print("YES")
            sw=True
            break
        i+=1
    if sw==False:
        print("NO")