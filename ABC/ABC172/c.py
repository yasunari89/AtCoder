n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = [0]
b = [0]
total = 0
for Ai in A:
    total += Ai
    a.append(total)
total = 0
for Bi in B:
    total += Bi
    b.append(total)

j = len(b) - 1
ans = 0
for i in range(len(a)):
    if a[i] > k:
        continue
    while a[i] + b[j] > k:
        j -= 1
        if j < 0:
            break
    ans = max(ans, i + j)

print(ans)