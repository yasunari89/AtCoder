X, Y, Z, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)

ABC = []
for a in range(X):
    for b in range(Y):
        if (a+1) * (b+1) > K:
            break
        else:
            pass
        for c in range(Z):
            if (a+1) * (b+1) * (c+1) > K:
                break
            else:
                ABC.append(A[a] + B[b] + C[c])

for i in range(K):
    print(sorted(ABC, reverse=True)[i])
