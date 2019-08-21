dishes = sorted([int(input()) for _ in range(5)], key=lambda x:int(str(x)[-1]))

for dish in dishes:
    if int(str(dish)[-1]) == 0:
        new_dishes = dishes[1:]
        new_dishes.append(dish)
        dishes = new_dishes
    else:
        pass

time = 0
for i, dish in enumerate(dishes):
    if i == 0:
        time += dish
    else:
        if dish % 10 != 0:
            rest = 10 - (dish % 10)
        else:
            rest = 0
        time += dish + rest

print(time)
