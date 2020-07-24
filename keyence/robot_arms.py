import numpy as np


N = int(input())
X = []
L = []
for _ in range(N):
    Xi, Li = map(int, input().split())
    X.append(Xi)
    L.append(Li)

begins = []
ends = []
for i in range(N):
    begins.append(X[i] - L[i])
    ends.append(X[i] + L[i])

b = []
e = []
for i in np.argsort(ends):
    b.append(begins[i])
    e.append(ends[i])
begins = b
ends = e

now = -1e9
cnt = 0
for i in range(N):
    if now <= begins[i]:
        cnt += 1
        now = ends[i]

print(cnt)