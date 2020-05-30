N = int(input())
arr = list(map(int, input().split()))

if N == 0:
    print(1 if arr[0]==1 else -1)
    exit()
elif arr[0] != 0:
    print(-1)
    exit()

# 末端の葉の数で初期化
sum_arr = [arr[-1]]*N
for i in range(1,N):
	# 深さi+1での頂点数 + 深さiでの葉の数
    sum_arr[i] = sum_arr[i-1]+arr[N-i]
# 本来の順番に反転
sum_arr = sum_arr[::-1]

# 二分木の根から見ていく
ans = [1]*(N+1)
for i in range(1,N+1):
    if ans[i-1]-arr[i-1] < 0:
        print(-1)
        exit()
    tmp = min((ans[i-1]-arr[i-1])*2,sum_arr[i-1])
    ans[i] = tmp

# 超注意
# このチェックはマジで忘れる
if ans[N] != arr[-1]:
    print(-1)
    exit()

print(sum(ans))
