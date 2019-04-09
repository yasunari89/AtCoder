N, M = map(int, input().split())
A = list(map(int, input().split()))

# 数字kに対するマッチ必要本数を返す
def num(k):
    costs = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    return costs[k-1]

# 動的計画法
# dp(i) := i本の最大桁数(i = 0,1,...,N)
# constructor
dp = [0 for _ in range(N+1)]

costs = [num(k) for k in A]
for i in range(1, N+1):
    for cost in costs:
        if i - cost < 0:
            pass
        else:
            temp = dp[i - cost] + 1
            dp[i] = max(dp[i], temp)

ans = ''
many = N
for _ in range(dp[N]):
    for k in sorted(A, reverse=True):
        if dp[many - num(k)] == dp[many] - 1:
            ans += str(k)
            many -= num(k)
            break
        else:
            pass

print(dp)
