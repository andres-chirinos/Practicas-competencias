def f(x):
    return sum([int(i) for i in str(x)])

n=int(input())
arr=list(map(int,input().split()))
for a_i in arr:
    s=0
    for i in range(len(arr)):
        s+=f(a_i+arr[i])
    print(s, end=" ")
