N = int(input())
h = list(map(int, input().split()))

new_h = [0] + h + [0]
# print(zero_h)
new_N = N + 2

zero_h = [0 for _ in range(new_N)]
counter = 0
flag = False
while_counter = 0
while(new_h != zero_h):
    # while_counter += 1
    # if while_counter > 15:
    #     break
    # print(new_h)
    for i in range(new_N):
        if flag == False:
            if new_h[i] == 0:
                start = i + 1
                flag = True
        elif flag == True:
            if new_h[i] == 0:
                end = i
                if new_h[start:end] == []:
                    start = i + 1
                    flag = True
                    pass
                else:
                    flag = False
                    new_h[start:end] = [new_h[i]-1 for i in range(start,end)]
                    counter += 1

print(counter)
