n = int(input())
a = list(map(int, input().split()))

rsort_a = sorted(a, reverse=True)
an = len(a)
i = 1
ans = sum(a)
add = rsort_a[0]
while i < an:
    rsort_ai = rsort_a[i]
    ans += add + rsort_ai
    add += rsort_ai
    i += 1
print(ans)