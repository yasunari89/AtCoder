from pprint import pprint
from time import sleep

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

start = Point()
goal = Point()

r, c = map(int, input().split())
start.y, start.x = map(int, input().split())
goal.y, goal.x = map(int, input().split())
start.y -= 1
start.x -= 1
goal.y -= 1
goal.x -= 1

maze = []
for _ in range(r):
    maze.append([l for l in input()])

queues = []
visited = [[False for _ in range(c)] for _ in range(r)]
times = [[99999999 for _ in range(c)] for _ in range(r)]

visited[start.y][start.x] = True
queues.append((start.y, start.x))
times[start.y][start.x] = 0
while len(queues) > 0:
    y, x = queues.pop(0)
    for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
        if maze[y+dy][x+dx] != '.':
            continue
        if visited[y+dy][x+dx]:
            continue
        visited[y+dy][x+dx] = True
        times[y+dy][x+dx] = times[y][x] + 1
        queues.append((y+dy, x+dx))

print(times[goal.y][goal.x])