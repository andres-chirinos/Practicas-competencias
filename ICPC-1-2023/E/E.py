N, K = map(int, input().split())
F = list(map(int, input().split()))
for _ in range(K):
  max_value=max(F)
  turn=sum(map(int,str(max_value)))
  F[F.index(max_value)]=max_value-turn
print(turn)