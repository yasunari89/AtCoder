N, K = map(int, input().split())
S = input()

# 累積和で実装

now = 1
cnt = 0
nums = []
for i in range(N):
    if int(S[i]) == now:
        cnt += 1
    else:
        nums.append(cnt)
        cnt = 1
        now = 1 - now
nums.append(cnt)
if int(S[-1]) == 0:
    nums.append(0)

# print(nums)

cumulative_sum = []
M = len(nums)
sum = 0
for i in range(M):
    sum += nums[i]
    cumulative_sum.append(sum)

# print(cumulative_sum)

ans = 0
start = 0
final = 2 * K
answers = []

# M = len(nums) = len(cumulative_sum)
if M < 2 * K + 1:
    print(len(S))
    exit()
if final <= M-1:
    while(final <= M-1):
        if start == 0:
            answers.append(cumulative_sum[final])
        else:
            ans = cumulative_sum[final] - cumulative_sum[start-1]
            answers.append(ans)

        # print(start, final, ans)
        start += 2
        final += 2
    print(max(answers))
else:
    print(cumulative_sum[0])

# print(answers)
