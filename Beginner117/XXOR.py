N, K = map(int, input().split())
A = list(map(int, input().split()))

def f(X): # O(1e5)
    sum = 0
    for i in range(N):
        sum += X ^ A[i]
    return sum

def bin_without0b(x):
    # str型
    return bin(x)[2:]

K_binary = bin(K)[2:]
K_binary_size = len(K_binary)
memo0 = [0 for _ in range(K_binary_size)]
# memo1 = [0 for _ in range(len(K_binary))]

# O(1e6)
for i in range(N): # O(1e5)
    for digit in range(-K_binary_size, 0): # O(42)
        Ai = bin(A[i])[2:].zfill(K_binary_size)
        if int(Ai[digit]) == 0:
            memo0[digit] += 1
        else:
            # memo1[digit] += 1
            pass
# print(memo0, memo1)

ansX = ''
for i in range(len(memo0)):
    if memo0[i] >= N/2:
        ansX += '1'
    else:
        ansX += '0'

if int(ansX, 2) > K:
    print(f(K))
else:
    print(f(int(ansX, 2)))
