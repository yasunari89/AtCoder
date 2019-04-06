import sys

antennas = []
for _ in range(5):
    antennas.append(int(input()))
k = int(input())

flag = 1
while(len(antennas) != 1):
    for i in range(len(antennas)-1):
        i += 1
        if antennas[i] - antennas[0] <= k:
            continue
        else:
            flag *= 0
            print(":(")
            sys.exit()
    antennas = antennas[1:]

if flag == 1:
    print('Yay!')
