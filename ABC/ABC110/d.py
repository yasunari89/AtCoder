from typing import List, Dict


def cumlative_sum(x: List) -> List:
    '''累積和'''
    res = [0]
    for i, v in enumerate(x):
        res.append(res[i] + v)
    return res
def prime_factorization(x: int) -> Dict[int, int]:
    '''
    素因数分解: output = Dict[素因数, 乗数]

    最大の素因数は高々sqrt(x)以下であることを利用して高速化
    '''
    divided = x
    res = {}
    max_possible_factor = int(x**0.5)
    for num in range(2, max_possible_factor + 1):
        if divided % num == 0:
            counter = 0
            while divided % num == 0:
                counter += 1
                divided //= num
            res[num] = counter
    
    if divided != 1:
        res[divided] = 1
    
    if res == {}:
        res[x] = 1

    return res
def factorial(x: int) -> int:
    '''階乗'''
    res = 1
    while x > 1:
        res *= x
        x -= 1
    return res
def combination(x: int, y: int) -> int:
    '''xCy'''
    res = 1
    for _ in range(y):
        res *= x
        x -= 1
    res //= factorial(y)
    return res

n, m = map(int, input().split())
prime_factors_dict = prime_factorization(m)
ans = 1
for power in prime_factors_dict.values():
    ans *= combination(power+n-1, n-1)
    if ans > 1000000000 + 7:
        ans %= 1000000000 + 7
print(ans)