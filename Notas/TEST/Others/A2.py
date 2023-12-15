from math import floor, log10

def count_digits(x, y):
  n_digits_x = int(floor(log10(max(abs(x), 1)))) + 1
  n_digits_y = int(floor(log10(max(abs(y), 1)))) + 1
  n_digits = n_digits_x + n_digits_y
  if 2 * x * 5 * y > 9:
    n_digits += 1

  return n_digits

x,y = map(int,input().split())
print(count_digits(x,y))