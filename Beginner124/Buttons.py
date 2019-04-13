buttons = list(map(int, input().split()))

ans = 0
ans_list = []

ans_list.append(2 * buttons[0] - 1)
ans_list.append(2 * buttons[1] - 1)
ans_list.append(buttons[0] + buttons[1])
print(max(ans_list))
