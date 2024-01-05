from types import _V_co


def max_sum_of_adjacent_elements(lst):

    for i in range(1, len(lst) - 1):
        current_sum = lst[i] + lst[i + 1]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Ejemplo de uso
mi_lista = [1, 3, -2, 4, 7, -1]
maxima_suma = max_sum_of_adjacent_elements(mi_lista)
print("La máxima suma de elementos contiguos es:", maxima_suma)


for _ in range(int(input())):
  n,m,k = map(int, input().split())#nºCities,nºdays,ºdaynotrain
  Vc = []
  max_sum = 0
  l,r = map(int, input().split())
  last_sum = abs(l-r)+1
  j=0
  for i in range(m):
    l,r = map(int, input().split())
    current_sum = abs(l-r)+1
    if current_sum+last_sum>max_sum:
      j=i
    last_sum=current_sum
  print(*Vc)
