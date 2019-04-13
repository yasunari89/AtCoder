N, K = map(int, input().split())
S = input()
intS = int(S)

calc_list = [1 if S[0] == '0' else 0]
for i in range(1, len(S)):
    if S[i] == '0':
        if S[i-1] == '1':
            calc_list.append(1)
        elif S[i-1] == '0':
            calc_list.append(calc_list[i-1] + 1)
    else:
        calc_list.append(0)

print(calc_list)

def zeros(calc_list):
    zero_list = [1 if calc_list[0] == 0 else 0]
    for i in range(1, len(calc_list)):
        if calc_list[i] == 0:
            zero_list.append(zero_list[i-1] + 1)
        else:
            zero_list.append(0)

    return zero_list


max_times = max(calc_list)
for _ in range(K):
    for i in range(len(calc_list)):
        if calc_list.count(max_times) == 1:
            if calc_list[i] == max_times:
                for j in range(max_times):
                    calc_list[i-j] = 0
                break
        else:
            zero_list = zeros(calc_list))
            index = zero_list.index(max(zero_list))

    print('calc', calc_list)
    print('zeros', zeros(calc_list))
    max_times = max(calc_list)
