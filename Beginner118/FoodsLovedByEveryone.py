N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split()))[1:])

flags = [0 for _ in range(M)]
counter = 0
for i in range(M):
    i += 1
    for j in range(N):
        if not i in A[j]:
            flags[i-1] = 0
            break
        else:
            flags[i-1] = 1
    i += 1
print(flags.count(1))
