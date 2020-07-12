alen, blen, time = map(int, input().split())
abooks = list(map(int, input().split()))
bbooks = list(map(int, input().split()))

counter = 0
reading_time = 0
while time > 0:
    if len(abooks) < 1 and len(bbooks) < 1:
        break
    elif len(abooks) < 1 and len(bbooks) > 0:
        reading_time = bbooks.pop(0)
    elif len(abooks) > 0 and len(bbooks) < 1:
        reading_time = abooks.pop(0)
    elif abooks[0] < bbooks[0]:
        reading_time = abooks.pop(0)
    else:
        reading_time = bbooks.pop(0)
    time -= reading_time
    if time >= 0:
        counter += 1

print(counter)