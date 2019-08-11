N = int(input())
ceil = 1000

for num in range(N, ceil):
    num = str(num)
    if num[0] == num[1] and num[0] == num[2]:
        print(int(num))
        break
    else:
        pass
