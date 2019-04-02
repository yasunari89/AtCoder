class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = [-1 for i in range(self.N)]

    def root(self, A):
        if self.parent[A] < 0:
            return A
        else:
            self.parent[A] = self.root(self.parent[A])
            return self.parent[A]

    def size(self, A):
        return -self.parent[self.root(A)]

    def connect(self, A, B):
        A = self.root(A)
        B = self.root(B)
        if A == B:
            return False
        elif self.size(A) < self.size(B):
            A, B = B, A
        else:
            pass
        self.parent[A] += self.parent[B]
        self.parent[B] = A
        return True

islands, bridges = map(int, input().split())
A, B = [], []
ans = [0 for i in range(bridges)]
ans[bridges-1] = int(islands * (islands-1) / 2)

UF = UnionFind(islands)

for i in range(bridges):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)

for i in range(bridges-1, 0, -1):
    if UF.root(A[i]) != UF.root(B[i]):
        ans[i-1] = ans[i] - UF.size(A[i]) * UF.size(B[i])
        UF.connect(A[i], B[i])
    else:
        ans[i-1] = ans[i]

for i in range(bridges):
    print(ans[i])
