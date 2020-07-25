n, mw = map(int, input().split())
v, w = [], []
for _ in range(n):
    vi, wi = map(int, input().split())
    v.append(vi)
    w.append(wi)

memo = [[0]*(mw+1) for _ in range(n+1)]
res = 0
def dfs(i, target_w):
    if i == n:
        res = 0
    elif memo[i][target_w] != 0:
        res = memo[i][target_w]
    elif target_w < w[i]:
        res = dfs(i + 1, target_w)
        memo[i][target_w] = res
    else:
        res = max(
            dfs(i + 1, target_w - w[i]) + v[i],
            dfs(i + 1, target_w)
        )
        memo[i][target_w] = res
    return res

print(dfs(0, mw))
