A, B, K = map(int, input().split())

def maxDivider(divider, divided):
    while(True):
        rest = divided % divider
        if rest == 0:
            return divider
        else:
            divided = divider
            divider = rest

def dividers(x):
    dividers = []
    divider = 1
    while(divider <= x / divider):
        if x % divider == 0:
            dividers.append(divider)
            if divider == int(x / divider):
                pass
            else:
                dividers.append(int(x / divider))
        else:
            pass
        divider += 1
    return sorted(dividers)

# set A <= B
if A > B:
    A, B = B, A
else:
    pass

ans = dividers(maxDivider(A, B))[-K]
print(ans)
