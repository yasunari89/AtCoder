n = int(input())
d = int(str(n)[-1])
t = {'bon':[3], 'pon':[0,1,6,8], 'hon':[2,4,5,7,9]}
for s in t:
  if d in t[s]:
    print(s)
