import math
A, B, T = map(int, input().split())
ans = B * math.floor((T + 0.5) / A)
print(ans)
