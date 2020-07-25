import numpy as np


n = int(input())
x, y, p = [], [], []
for _ in range(n):
    xi, yi, pi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    p.append(pi)

rsort_indexes = np.argsort(p)[::-1]
rsort_x, rsort_y, rsort_p = [], [], []
for i in rsort_indexes:
    rsort_x.append(x[i])
    rsort_y.append(y[i])
    rsort_p.append(p[i])

rails_x = [0]
rails_y = [0]
on_rail = [False for _ in range(n)]

s = 0
for ki in range(1):
    for ni in range(n):
        rx, ry = rsort_x[ni], rsort_y[ni]
        d = min(
            min(abs(np.array([rx]*len(rails_x)) - np.array(rails_x))), 
            min(abs(np.array([ry]*len(rails_y)) - np.array(rails_y)))
        )
        s += rsort_p[ni] * d

