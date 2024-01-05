"""n = int(input())
nums = list(map(int, input().split()))
power_set = set()
for i in range(2**n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(nums[j])
    if 1 in subset:
      power_set.add(subset)
print(len(power_set))"""

N = int(input())
sequence = list(map(int, input().split()))

contador = 0
contador_unos = 0

for i in range(N):
    if sequence[i] == 1:
        contador_unos += 1

    if contador_unos % 2 != 0:
        contador += 1

print(contador)
