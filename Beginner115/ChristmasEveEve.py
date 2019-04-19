N = int(input())
max_p = 0
sum = 0
for i in range(N):
  pi = int(input())
  sum += pi
  max_p = max(max_p, pi)

ans = int(sum - max_p / 2)
print(ans)
