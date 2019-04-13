S = input()

white_counter = 0
tile_color = '1'
for tile in S:
    if tile_color == tile:
        pass
    else:
        white_counter += 1
    if tile_color == '1':
        tile_color = '0'
    else:
        tile_color = '1'

black_counter = 0
tile_color = '0'
for tile in S:
    if tile_color == tile:
        pass
    else:
        black_counter += 1
    if tile_color == '1':
        tile_color = '0'
    else:
        tile_color = '1'

print(min(white_counter, black_counter))
