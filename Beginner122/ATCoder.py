words = list(input())
binary_list = []
for word in words:
  if word == "A" or word == "T" or word == "C" or word == "G":
      binary_list.append(1)
  else:
      binary_list.append(0)
max_counter = 0
for first in range(len(binary_list)):
    counter = 0
    multi = 1
    if binary_list[first] == 1:
        while(multi):
            multi *= binary_list[first]
            if multi == 0:
                break
            counter += 1
            if counter >= max_counter:
                max_counter = counter
            if first == len(binary_list) - 1:
                break
            else:
                first += 1
print(max_counter)
