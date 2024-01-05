rotate = lambda arr: [arr[-1]] + arr[:-1]
all_equal = lambda lst: all(x == lst[0] for x in lst)
suma = lambda arr0,arr1: [x + y for x, y in zip(arr0, arr1)]

def sort_for_equal_sum(arr0, arr1):
    arr0.sort()
    arr1.sort(reverse=True)
    return arr0, arr1

for _ in range(int(input())):


    N = int(input())
    arr0 = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    arr0, arr1 = sort_for_equal_sum(arr0, arr1)

    if all_equal(suma(arr0, arr1)):
        print(*arr0)
        print(*arr1)
    else:
        print(-1)
    
