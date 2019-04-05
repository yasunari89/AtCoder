def divisors(x):
    '''公約数をリスト型で返す関数'''
    divisors = []
    divisor = 1
    while(divisor <= x / divisor):
        if x % divisor == 0:
            divisors.append(divisor)
            if divisor == int(x / divisor):
                pass
            else:
                divisors.append(int(x / divisor))
        else:
            pass
        divisor += 1
    return sorted(divisors)

A, B = map(int, input().split())

if A in divisors(B):
    print(A + B)
else:
    print(B - A)
