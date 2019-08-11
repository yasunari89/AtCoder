K, X = map(int, input().split())

first_point = X - K + 1
last_point = X + K - 1

if first_point < -1000000:
    first_point = -1000000
if last_point > 1000000:
    last_point = 1000000

for _ in range(first_point, last_point+1):
    print(_)
