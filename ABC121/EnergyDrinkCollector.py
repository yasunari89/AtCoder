N, M = map(int, input().split())
AB = []
for i in range(N):
    Ai, Bi = map(int, input().split())
    AB.append([Ai, Bi])

# # Bubble Sort
# start = 0
# for i in range(N-1):
#     for index in range(start, N-1):
#         if AB[index][0] > AB[index+1][0]:
#             AB[index], AB[index+1] = AB[index+1], AB[index]
#         else:
#             pass
#         start += 1

AB = sorted(AB, key=lambda x: x[0])

final = 0
sum_bottles = 0
while(M > sum_bottles):
    final += 1
    sum_bottles += AB[final-1][1]

cost = 0
sum_bottles = 0
for i in range(final):
    if i == final - 1:
        cost += AB[i][0] * (M - sum_bottles)
    else:
        cost += AB[i][0] * AB[i][1]
        sum_bottles += AB[i][1]

print(cost)
