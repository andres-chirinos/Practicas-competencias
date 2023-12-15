n=int(input())
arr=list(map(int,input().split()))
if (sum(arr)/n)%3==0:
    print("N")
else:
    print("Y")
