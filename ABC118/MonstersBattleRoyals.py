def maxDivisor(divisor, divided):
    '''最大公約数を返す関数'''
    while(True):
        rest = divided % divisor
        if rest == 0:
            return divisor
        else:
            divided = divisor
            divisor = rest


N = int(input())
A = list(map(int, input().split()))

inf = 1 * 10**9
ans = inf
for i in range(len(A)):
    if i == len(A) - 1:
        break
    else:
        ans = min(ans, maxDivisor(A[i], A[i+1]))

print(ans)
