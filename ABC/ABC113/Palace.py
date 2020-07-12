N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
temperatures = []
for i in range(N):
    temperatures.append(T - H[i] * 0.006)
# print(temperatures)
diff = 10**9
ans = -1
for i in range(N):
    new_diff = abs(temperatures[i] - A)
    if diff > new_diff:
        diff = new_diff
        ans = i

print(ans+1)
