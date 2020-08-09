import sys
sys.setrecursionlimit(int(1e8))


s = input()
n = len(s)

def rec(op_index, part_s):
    if op_index == n - 1:
        return sum(map(int, part_s.split('+')))
    part_s1 = '{}{}'.format(part_s, s[op_index+1])
    part_s2 = '{}+{}'.format(part_s, s[op_index+1])
    return rec(op_index+1, part_s1) + rec(op_index+1, part_s2)

print(rec(0, s[0]))