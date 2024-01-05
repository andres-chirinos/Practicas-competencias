def main():
  s=input()
  t=input()
  T = [t[i-1]==t[i] for i in range(1,len(t))]
  
  while True:
    S = [s[i-1]==s[i] for i in range(1,len(s))]
    if not any(S):
      return "yes"
    if (any(S) and any(T)):
      return "no"
    try:
      i = S.index(True)
    except:
      break

    if not (s[i]!=t[0] and s[i+1]!=t[-1]):
      return "no"
    s=s[:i]+t+s[i+1:]
  return "yes"

for _ in range(int(input())):
  n,m = map(int, input().split())
  print(main())