c = input()
K = int(input())
r = c
while True:
  c=r
  for i in range(len(c)//K):
    chars = list(c)
    chars[i], chars[i + K] = chars[i + K], chars[i]
    if (a:=''.join(chars)) < r: r=a
  if c==r:
    break
print(r) 
