n=int(input())
arr=[int(x) for x in input().split() if ((int(x)%3==0 or int(x)%2==0) and int(x)%6!=0)]
print(len(arr))