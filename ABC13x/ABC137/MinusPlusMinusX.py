import numpy as np

A, B = map(int, input().split())
max_num = max(
    A + B,
    A - B,
    A * B,
)
print(max_num)
