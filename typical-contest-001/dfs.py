from pprint import pprint

height, width = map(int, input().split())
maze = []
for _ in range(height):
    row = [l for l in input()]
    maze.append(row)

reached = [[False for _ in range(width)] for _ in range(height)]
def search(x, y):
    if x < 0 or y < 0:
        return 
    if x > height - 1 or y > width - 1:
        return 
    if maze[x][y] == '#':
        return
    if reached[x][y] == True:
        return 
    
    reached[x][y] = True
    search(x+1, y)
    search(x, y+1)
    search(x-1, y)
    search(x, y-1)

search(0, 0)
pprint(reached)