n = int(input())
mod = 10**9 + 7
# memo[len][c1][c2][c3]
dp = [[[[0, 0, 0, 0] for k in range(4)] for j in range(4)] for i in range(n+1)]

# ACGT => 0123とする。
# 長さ0の文字数は1である。
# 0,1,2に関する制約しかないので文字列sは333sと考えても良い。
dp[0][3][3][3] = 1

for len in range(n):
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                if dp[len][c1][c2][c3] == 0:
                    continue
                for add in range(4):
                    if c1 == 1 and c2 == 0 and add == 2:
                        continue
                    elif c1 == 0 and c2 == 1 and add == 2:
                        continue
                    elif c1 == 2 and c2 == 0 and add == 1:
                        continue
                    elif c1 == 1 and c3 == 0 and add == 2:
                        continue
                    elif c2 == 1 and c3 == 0 and add == 2:
                        continue
                    dp[len+1][add][c1][c2] += dp[len][c1][c2][c3]
                    dp[len+1][add][c1][c2] %= mod
    ans = 0
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                ans += dp[n][c1][c2][c3]
                ans %= mod

print(ans)
