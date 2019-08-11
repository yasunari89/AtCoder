N, K = map(int, input().split())
h = sorted([int(input()) for i in range(N)])
# print(h)

inf = 10**9
min_height = inf
for i in range(N-K+1):
    # print(i+(K-1), h[i+(K-1)], i, h[i])
    min_height = min(min_height, h[i+(K-1)] - h[i])

print(min_height)
