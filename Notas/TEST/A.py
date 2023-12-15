n, k = (int(x) for x in input().split(" "))
a = [y for x in input().split(" ") if (y:=int(x))>0]
print(len(a[:k]))