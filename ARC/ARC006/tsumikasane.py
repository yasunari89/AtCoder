N = int(input())
w = [int(input()) for _ in range(N)]

cnt = 0
tops = []
for i, wi in enumerate(w):
    if tops == []:
        tops.append(wi)
        cnt += 1
    else:
        for j, top in enumerate(tops):
            if top >= wi:
                tops.pop(j)
                cnt -= 1
                break
        tops.append(wi)
        cnt += 1
        tops.sort()

print(cnt)
