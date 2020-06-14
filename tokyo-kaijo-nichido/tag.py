a, v1 = map(int, input().split())
b, v2 = map(int, input().split())
t = int(input())
l = abs(a-b)
delta_v = v1-v2
if delta_v <= 0:
  print("NO")
  exit()

if delta_v * t >= l:
  print("YES")
else:
  print("NO")

