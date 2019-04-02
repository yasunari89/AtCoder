from Errors import Errors


def maxDivisor(divisor, divided):
    '''最大公約数を返す関数'''
    if divisor > divided:
        print(Errors.reverse_variables_error.value)
    elif type(divisor) != int or type(divided) != int:
        print(Errors.not_int_error.value)
    else:
        while(True):
            rest = divided % divisor
            if rest == 0:
                return divisor
            else:
                divided = divisor
                divisor = rest


def divisors(x):
    '''公約数をリスト型で返す関数'''
    if type(x) != int:
        print(Errors.not_int_error.value)
    else:
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


def XORfromZERO(x):
    '''
    Σ[0:(x-1)]Π(n xor (n+1))を返す関数
    つまり0からxまでの全ての整数をXORする関数
    '''
    if type(x) != int:
        print(Errors.not_int_error.value)
    elif x < 0:
        print(Errors.not_zero_and_over_error.value)
    else:
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


def factorial(n):
    'n!を返す関数。'
    if type(n) != int:
        print(Errors.not_int_error.value)
    else:
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
    if type(n) != int or type(r) != int:
        print(Errors.not_int_error.value)
    else:
        ans = factorial(n) / (factorial(r) * factorial(n-r))
        return int(ans)
