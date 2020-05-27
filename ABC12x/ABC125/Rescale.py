N = int(input())
Vs = list(map(int, input().split()))
Cs = list(map(int, input().split()))

diff = []
for i in range(N):
    diff.append(Vs[i]-Cs[i])
ans = 0
for i in range(N):
    if diff[i] > 0:
        ans += diff[i]
    else:
        pass
print(ans)
