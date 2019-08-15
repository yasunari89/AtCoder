from typing import List, Dict

N: int = int(input())
H: List[int] = list(map(int, input().split()))

used_index: List[bool] = [False for _ in range(N)]
while (True):
    H_max_index: int = H.index(max(H))
    H[H_max_index] -= 1
    if not used_index[H_max_index]:
        used_index[H_max_index] = True
    else:
        print('No')
        break
    if max(H) == H[-1]:
        print('Yes')
        break
