n, mw = map(int, input().split())
v, w = [], []
for _ in range(n):
    vi, wi = map(int, input().split())
    v.append(vi)
    w.append(wi)

dp = [[0]*(mw+1) for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(mw+1):
        if j < w[i]:
            dp[i][j] = dp[i+1][j]
        else:
            dp[i][j] = max(
                dp[i+1][j],
                dp[i+1][j-w[i]] + v[i]
            )

print(dp[0][mw])