A, B = map(int, input().split())

# summary = A
# for XORed in range(A+1, B+1):
#     summary = summary ^ XORed

def XORfromZERO(x):
    rest = x % 2
    quotient = (x + rest) / 2
    if rest == 0:
        if quotient % 2 == 0:
            return 0 ^ x
        else:
            return 1 ^ x
    else:
        if quotient % 2 == 0:
            return 0
        else:
            return 1

print(XORfromZERO(A-1) ^ XORfromZERO(B))
