from collections import defaultdict

def lcs(X,Y):
    m,n=len(X),len(Y)
    L=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0: L[i][j]=0
            elif X[i-1]==Y[j-1]: L[i][j]=L[i-1][j-1]+1
            else: L[i][j]=max(L[i-1][j],L[i][j-1])
    return L[m][n]

book=[input() for _ in range(int(input()))]
for _ in range(int(input())):
    q,k = input().split()
    k=int(k)
    lista = defaultdict(set)
    for p in book:
        lista[lcs(q,p)].add(p)
    search = sorted(lista[max(lista.keys())])
    if len(search)<k:
        print(-1)
    else:
        print(book.index(search[k%len(search)-1])+1)
