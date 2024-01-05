import heapq

def max_k_sums(arr, k):
    heapq.heapify(arr)
    while len(arr) > k:
        num1 = -heapq.heappop(arr)
        num2 = -heapq.heappop(arr)
        heapq.heappush(arr, -(num1 + num2))
    return arr

n,k = map(int, input().split())
arr_0 = list(map(int, input().split()))
if n<k:
    print(0)
else:
    print(min(max_k_sums(arr_0, k)))
