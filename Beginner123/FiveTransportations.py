_ = [int(input()) for __ in range(6)]
N = _[0]
cities = _[1:]

sorted_cities = sorted(cities)
if N % sorted_cities[0] == 0:
    times = N / sorted_cities[0]
else:
    times = (N - N % sorted_cities[0]) / sorted_cities[0] + 1
print(int(times + 4))
