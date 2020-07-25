n, k = map(int, input().split())
a = list(map(int, input().split()))

previ = 0
nowi = k
for _ in range(n-k):
    prev = a[previ]
    now = a[nowi]
    if now > prev:
        print('Yes')
    else:
        print('No')
    previ += 1
    nowi += 1