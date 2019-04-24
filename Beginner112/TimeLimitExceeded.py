N, T = map(int, input().split())
ct = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
# print(ct)

for i in range(N):
    if ct[i][1] <= T:
        print(ct[i][0])
        break
    else:
        if i == N - 1:
            print('TLE')
