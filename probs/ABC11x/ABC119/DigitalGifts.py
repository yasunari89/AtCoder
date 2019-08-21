many = int(input())
sum_money = 0
for i in range(many):
    money, currency = map(str, input().split())
    if currency == 'JPY':
        sum_money += int(money)
    else:
        sum_money += 3.8e5 * float(money)
        # 以下のコードではinfしてしまう。
        # sum_money += 380000 * float(money)

print(sum_money)
