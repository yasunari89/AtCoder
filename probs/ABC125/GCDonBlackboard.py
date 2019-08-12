import fractions as f
N = int(input())
As = list(map(int, input().split()))
ans = 0

for i in range(N):
    new_As = As.copy()
    new_As.pop(i)
    a = new_As[0]
    for j in range(1, N-1):
        b = new_As[j]
        a = f.gcd(a, b)
    ans = max(ans, a)
print(ans)
