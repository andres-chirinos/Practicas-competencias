n = int(input())
a = list(map(int, input().split()))
max_a = max(a)
if max_a <= a[0] and a.count(max_a) == 1:
    print(0)
else:
    print(abs(max_a-a[0])+1)