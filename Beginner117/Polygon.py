N = int(input())
Ls = sorted(list(map(int, input().split())))

sum = 0
for i in range(N-1):
    sum += Ls[i]

if sum > Ls[-1]:
    print('Yes')
else:
    print('No')
