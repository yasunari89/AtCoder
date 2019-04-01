def maxDivisor(divisor, divided):
    '''最大公約数を返す関数'''
    if divisor > divided:
        print("Error: 引数の順番が逆！")
    elif type(divisor) != int or type(divided) != int:
        print("Error: 引数はint型に！")
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
        print("Error: 引数はint型に！")
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
