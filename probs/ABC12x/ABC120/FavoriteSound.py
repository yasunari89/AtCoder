cost, wallet, many = map(int, input().split())

if wallet >= cost * many:
    ans = int(many)
else:
    ans = int((wallet - (wallet % cost)) / cost)

print(ans)
