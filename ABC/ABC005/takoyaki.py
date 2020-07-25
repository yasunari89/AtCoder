import sys


T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

if N < M:
    print('no')
    sys.exit()

BB = [b - T for b in B]
BE = B

bn = len(BB)

for bi in range(bn):
    bb = BB[bi]
    be = BE[bi]
    can_sell = False
    for a in A:
        if bb <= a <= be:
            can_sell = True
            ai = A.index(a)
            A.pop(ai)
            break
    if can_sell == False:
        print('no')
        sys.exit()
print('yes')
