from typing import List, Dict

N: int = int(input())
A: List[int] = list(map(int, input().split()))
B: List[int] = list(map(int, input().split()))

C: List[int] = A.copy()
for i in range(N):
    if C[i] - B[i] > 0:
        C[i] -= B[i]
    else:
        C[i+1] = C[i+1] - (B[i] - C[i]) if C[i+1] - (B[i] - C[i]) > 0 else 0
        C[i] = 0

beaten_monster: int = sum(A) - sum(C)
print(beaten_monster)
