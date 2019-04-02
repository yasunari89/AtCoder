from Errors import Errors

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
