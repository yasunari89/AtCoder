h, w, k = map(int, input().split())
table = []
for _ in range(h):
    table.append([l for l in input()])

ans = 0
for rbit in range(1 << h):
    for cbit in range(1 << w):
        black = 0
        for i in range(h):
            for j in range(w):
                if (rbit >> i) & 1 == 0 and (cbit >> j) & 1 == 0 and table[i][j] == '#':
                    black += 1
        if black == k:
            ans += 1
print(ans)