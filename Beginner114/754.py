S = input()
N = len(S)
diff = 10**9
for i in range(N-2):
    diff = min(abs(753 - int(S[i:i+3])), diff)

print(diff)
