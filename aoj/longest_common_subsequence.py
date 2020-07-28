import sys
from pprint import pprint
sys.setrecursionlimit(10**8)


n = int(input())
strs = []
for _ in range(n):
    str1 = [e for e in input()]
    str2 = [e for e in input()]
    strs.append((str1, str2))

for str1, str2 in strs:

    memo = [[0]*len(str2) for _ in range(len(str1))]
    def rec(i1, i2):
        if i1 < 0 or i2 < 0:
            return 0

        if memo[i1][i2] > 0:
            return memo[i1][i2]

        if str1[i1] == str2[i2]:
            res = rec(i1 - 1, i2 - 1) + 1
        else:
            res = max(rec(i1 - 1, i2), rec(i1, i2 - 1))
        memo[i1][i2] = res
        return res
    

    n1 = len(str1)
    n2 = len(str2)
    print(rec(n1 - 1, n2 - 1))
