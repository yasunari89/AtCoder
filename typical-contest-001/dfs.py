from pprint import pprint

height, width = map(int, input().split())
maze = []
for _ in range(height):
    row = [l for l in input()]
    maze.append(row)

class Start:
    def __init__(self):
        self.x = 0
        self.y = 0
class Goal:
    def __init__(self):
        self.x = 0
        self.y = 0

start = Start()
goal = Goal()
for x in range(height):
    for y in range(width):
        if maze[x][y] == 's':
            start.x, start.y = x, y
        if maze[x][y] == 'g':
            goal.x, goal.y = x, y

# Fill-out DFS
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

search(start.x, start.y)
if reached[goal.x][goal.y] == True:
    print('Yes')
else:
    print('No')