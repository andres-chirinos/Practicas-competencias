def count_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
 
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 1
 
    for i in range(3, n + 1):
        ways[i] = ways[i - 2] + ways[i - 1]
 
    return ways[n]
 
# Input
n = int(input())
 
# Output
print(count_ways(n))