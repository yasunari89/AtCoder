X, Y = map(int, input().split())

cnt = 0
while X <= Y:
    cnt += 1
    X *= 2
print(cnt)