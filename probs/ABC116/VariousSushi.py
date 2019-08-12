N, K = map(int, input().split())
td = []
for i in range(N):
    ti, di = map(int, input().split())
    td.append([ti, di])

# input:tdの整理
td = sorted(td, key=lambda x: x[0])
# print(td)
for i in range(N-1):
    td_forward = td[i]
    td_backward = td[i+1]
    if td_forward[0] == td_backward[0]:
        if td_forward[1] > td_backward[1]:
            td[i] = td_backward
            td[i+1] = td_forward
        else:
            pass
    else:
        pass
# print(td)
