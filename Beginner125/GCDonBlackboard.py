import fractions as f
N = int(input())
As = list(map(int, input().split()))
ans = 1

for i in range(N):
    new_As = As.copy()
    new_As.pop(i)
    new_As = sorted(new_As)
    if len(new_As) == 1:
        ans = max(ans, new_As[1])
    else:
        ans = max(ans, f.gcd(new_As[0], new_As[1]))

print(ans)
