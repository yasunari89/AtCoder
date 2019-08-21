A, B = map(int, input().split())
K: int = int((A + B) / 2)
K_float: float = (A + B) / 2

if K == K_float:
    print(K)
else:
    print('IMPOSSIBLE')
