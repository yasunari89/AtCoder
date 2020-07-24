import sys


Sp = [c for c in input()]
T = [c for c in input()]

sn = len(Sp)
tn = len(T)

match_i = 51
for i in range(sn - tn + 1):
    partial = Sp[i:i+tn]
    for j in range(len(partial)):
        if partial[j] == '?':
            partial[j] = T[j]
    if partial == T:
        match_i = i

if match_i > 50:
    print('UNRESTORABLE')
    sys.exit()

Sp[match_i:match_i+tn] = T
for i in range(sn):
    if Sp[i] == '?':
        Sp[i] = 'a'
S = ''.join(Sp)

print(S)