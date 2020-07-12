n = int(input())
nums = list(map(int, input().split()))

if 0 in nums:
  print(0)
  exit()

out = 1
for num in nums:
  out *= num
  if out > 1e18:
    print(-1)
    exit()
print(out)
  

