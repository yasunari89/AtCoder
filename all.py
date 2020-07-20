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

