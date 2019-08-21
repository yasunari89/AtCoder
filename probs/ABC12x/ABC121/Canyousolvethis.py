N, M, C = map(int, input().split())
B = list(map(int, list(input().split())))
A = []
for i in range(N):
    A.append(list(map(int, list(input().split()))))

counter = 0
for i in range(N):
    recog = 0
    for j in range(M):
        recog += A[i][j]*B[j]
    recog += C
    if recog > 0:
        counter += 1
print(counter)
