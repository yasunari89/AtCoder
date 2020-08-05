N, M = map(int, input().split())
companies = []
job_hunters = []
for _ in range(N):
    a, b, c, w = map(int, input().split())
    companies.append((a, b, c, w))
for _ in range(M):
    x, y, z = map(int, input().split())
    job_hunters.append((x, y, z))

dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
for a, b, c, w in companies:
    dp[a][b][c] = max(dp[a][b][c], w)

for i in range(101):
    for j in range(101):
        for k in range(101):
            si = max(i - 1, 0)
            sj = max(j - 1, 0)
            sk = max(k - 1, 0)
            dp[i][j][k] = max(
                dp[i][j][k], 
                dp[si][j][k],
                dp[i][sj][k],
                dp[i][j][sk]
            )

for x, y, z in job_hunters:
    print(dp[x][y][z])

