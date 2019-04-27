import fractions as f
import heapq
N = int(input())
As = list(map(int, input().split()))
ans = 1

for i in range(N):
    new_As = As.copy()
    new_As.pop(i)
    # new_As = sorted(new_As)
    mins = heapq.nsmallest(2, new_As)
    if len(new_As) == 1:
        ans = max(ans, mins[0])
    else:
        ans = max(ans, f.gcd(mins[0], mins[1]))

print(ans)
