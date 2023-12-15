d,m=map(int,input().split())
year=[31,28,31,30,31,30,31,31,30,31,30,31]
m-=1
while m>0:
  d+=year[m]
  m-=1
print(d-1)