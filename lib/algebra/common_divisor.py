def maxDivisor(divisor, divided):
    '''最大公約数を返す関数'''
    while(True):
        rest = divided % divisor
        if rest == 0:
            return divisor
        else:
            divided = divisor
            divisor = rest


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


def factorial(n):
    'n!を返す関数。'
    ans = 1
    while(n > 0):
        ans *= n
        n -= 1
    return ans


def nCr(n, r):
    '''
    nCrを返す関数。
    階乗を返すfactorial()関数に依存している。
    過剰を利用しているので、rが小さい時はここで計算量を取られていs舞うので使わない方が良い。
    組み合わせの値は必ず整数値になるのでintとしてreturnしている。
    '''
    ans = factorial(n) / (factorial(r) * factorial(n-r))
    return int(ans)
