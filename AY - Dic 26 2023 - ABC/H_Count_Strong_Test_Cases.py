MOD = 998244353
N = int(input())
fact = [1]*(2*N+1)
inv = [1]*(2*N+1)
invfact = [1]*(2*N+1)
for i in range(1,2*N+1):
    fact[i] = i*fact[i-1]%MOD
    inv[i] = pow(i,MOD-2,MOD)
    invfact[i] = inv[i]*invfact[i-1]%MOD
def C(n,k):
    if n<k or n<0 or k<0:
        return 0
    return fact[n]*invfact[k]*invfact[n-k]%MOD
def solve(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] = dp[i-1]*2%MOD
    dp2 = [0]*(n+1)
    dp2[0] = 1
    for i in range(1,n+1):
        dp2[i] = (dp2[i-1]+dp[i-1])%MOD
    ans = fact[2*n]
    for i in range(1,n+1):
        ans -= fact[2*n]*invfact[i]%MOD*invfact[2*n-i]%MOD*2%MOD*dp2[n-i]%MOD
        ans %= MOD
    for i in range(n+1,2*n+1):
        ans -= fact[2*n]*invfact[i]%MOD*invfact[2*n-i]%MOD*dp2[2*n-i]%MOD
        ans %= MOD
    return ans
print(solve(N))