def transformada(x):
  if x=="Mon": 
    return 0
  elif x=="Tue":
    return 1 
  elif x=="Wed":
    return 2
  elif x=="Thu":
    return 3
  elif x=="Fri":
    return 4
  elif x=="Sat":
    return 5
  elif x=="Sun":
    return 6
  else:
    return int(x)

T, N = map(transformada, input().split(" "))
mint=None
for x in input().split(" "):
  t=30-int(x)
  if t<0:
    t=int(x)
  elif (t+T)%7==5:
    t+=2
  elif (t+T)%7==6:
    t+=1
  if mint==None or mint>t:
    mint=t
print(mint)