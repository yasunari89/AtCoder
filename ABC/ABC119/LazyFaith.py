import bisect

shrines_many, temples_many, x_many = map(int, input().split())
shrine_positions = [int(input()) for _ in range(shrines_many)]
temple_positions = [int(input()) for _ in range(temples_many)]

inf = int(1e20)
shrine_positions = [-inf] + sorted(shrine_positions) + [inf]
temple_positions = [-inf] + sorted(temple_positions) + [inf]

# s_a, s_b, t_c, t_dを求める。
for _ in range(x_many):
    x = int(input())
    b = bisect.bisect_right(shrine_positions, x)
    d = bisect.bisect_right(temple_positions, x)
    min_distance = inf
    for shrine_position in [shrine_positions[b-1], shrine_positions[b]]:
        for temple_position in [temple_positions[d-1], temple_positions[d]]:
            distance1 = abs(x - shrine_position) + abs(shrine_position - temple_position)
            distance2 = abs(x - temple_position) + abs(shrine_position - temple_position)
            min_distance = min(min_distance, distance1, distance2)

    print(min_distance)
