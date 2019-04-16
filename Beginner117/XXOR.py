N, K = map(int, input().split())
A = list(map(int, input().split()))

def f(X):
    sum = 0
    for i in range(N):
        sum += X ^ A[i]
    return sum

ans = 0
for X in range(K+1):
    ans = max(ans, f(X))

print(ans)
