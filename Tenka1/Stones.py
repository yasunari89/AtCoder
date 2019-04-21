N = int(input())
S = input()
binS = []
for i in range(N):
    if S[i] == '.':
        binS.append(0)
    else:
        binS.append(1)
# print(binS)

# dp = [0]
# for i in range(1, N):
#     if binS[i-1] == 1 and binS[i] == 0:
#         dp.append(dp[i-1]+1)
#     else:
#         dp.append(dp[i-1])
#
# print(dp[-1])
first_counter = 0
second_counter = 0
if N % 2 == 1:
    half_N = (N - 1) / 2
    rest = 1
else:
    half_N = N / 2
    rest = 0

for i in range(half_N):
    if binS[i] == 0:
        first_counter += 1
for i in range(half_N, N):
    if binS[i] == 1:
        second_counter += 1
