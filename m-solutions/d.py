n = int(input())
a = list(map(int, input().split()))

stock = 0
money = 1000
prev_trend = a[1] - a[0]

if prev_trend > 0:
    stock += money // a[0]
    money -= a[0] * (money // a[0])

if len(a) > 2:
    for i in range(1, n-1):
        next_trend = a[i+1] - a[i]
        if prev_trend >= 0 and next_trend < 0:
            money += a[i] * stock
            stock = 0
        elif prev_trend <= 0 and next_trend > 0:
            stock += money // a[i]
            money -= a[i] * (money // a[i])
        prev_trend = a[i+1] - a[i]

money += a[n-1] * stock
stock = 0

print(money)