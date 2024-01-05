for _ in range(int(input())):
    N,X,Y = map(int,input().split())
    if (X+Y//3)/N>=2 and X>=N:
        print("YES")
    else:
        print("NO")