X, Y, Z, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
all = sorted(A + B + C)

def sumABC(a, b, c):
    return A[indices[0]-a] + B[indices[1]-b] + C[indices[2]-c]

indices = [-1, -1, -1]
for times in range(K):
    if times == 0:
        print(A[indices[0]] + B[indices[1]] + C[indices[2]])
    else:
        ret0 = sumABC(1, 0, 0)
        ret1 = sumABC(0, 1, 0)
        ret2 = sumABC(0, 0, 1)
        print(max(ret0, ret1, ret2))
        if max(ret0, ret1, ret2) == ret0:
            indices[0] += -1
        elif max(ret0, ret1, ret2) == ret1:
            indices[1] += -1
        else:
            indices[2] += -1
