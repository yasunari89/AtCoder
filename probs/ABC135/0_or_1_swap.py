from typing import List

N: int = int(input())
p: List[int] = list(map(int, input().split()))

index_not_equal_value_counter: int = 0
yes_or_no_flag: bool = True
for i, v in enumerate(p):
    i = i + 1
    if i != v:
        index_not_equal_value_counter += 1
    if index_not_equal_value_counter > 2:
        yes_or_no_flag = False

if yes_or_no_flag:
    print('YES')
else:
    print('NO')
