import numpy as np

N: int = int(input())
max_power: int = int(np.log10(N))
counter: int = 0
for power in range(1, max_power+1, 2):
    counter += 10 ** power - 10 ** (power - 1)
if max_power % 2 == 0:
    counter += N - 10 ** max_power + 1
else:
    pass
print(counter)
