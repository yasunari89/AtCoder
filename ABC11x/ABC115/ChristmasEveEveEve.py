D = int(input())
days = sorted([i for i in range(22, 26)], reverse=True)

c = 'Christmas'
for i, day in enumerate(days):
    if D == day:
        for _ in range(i):
            c += ' Eve'
        print(c)
