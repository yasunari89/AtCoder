X, Y, Z, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
all = sorted(A + B + C)

indices = [-1, -1, -1]

def sumABC(a, b, c):
    return A[indices[0]-a] + B[indices[1]-b] + C[indices[2]-c]

print("answers")
i = 0
while(i < K):
    ret0 = sumABC(0, 0, 0)
    ret1 = sumABC(1, 0, 0)
    ret2 = sumABC(0, 1, 0)
    ret3 = sumABC(0, 0, 1)
    ret4 = sumABC(1, 1, 0)
    ret5 = sumABC(1, 0, 1)
    ret6 = sumABC(0, 1, 1)
    ret7 = sumABC(1, 1, 1)
    returns = sorted([ret0, ret1, ret2, ret3, ret4, ret5, ret6, ret7])
    for j in range(7, -1, -1):
        i += 1
        print(returns[j])
    for _ in range(3):
        indices[_] += -1
