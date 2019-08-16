from typing import List

N: int = int(input())
H: List[int] = list(map(int, input().split()))

exit_flag: bool = False
# 操作が「小さくする」なので走査もreverseして
# 小さいかどうかを調べるようにする
for i in range(N-1, 0, -1):
    if H[i-1] - H[i] == 1:
        H[i-1] -= 1
    elif H[i-1] - H[i] > 1:
        exit_flag = True
        print('No')
        break

if not exit_flag:
    print('Yes')
