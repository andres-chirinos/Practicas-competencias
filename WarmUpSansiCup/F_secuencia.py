n = int(input())
def f(ni):
  if ni<=1:
    return 3
  return f(ni-1)+(2*(ni-2)-1)
 
s=0
for i in range(n):
  s+=f(i+1)
print(s-1)