S = list(input())
N = len(S)

counter = 0
i = 0
while(True):
    if not '0' in S or not '1' in S or S == []:
        break
    elif (S[i] == '1' and S[i+1] == '0') or (S[i] == '0' and S[i+1] == '1'):
        S.pop(i)
        S.pop(i)
        counter += 2
        i -= 1
    else:
        i += 1

print(counter)
