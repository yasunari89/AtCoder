T = int(input())
for _ in range(T):
  N,a,b,c,d = map(int, input().split())
  
  memo = {}
  def solve(n):
    if n == 0:
      return 0
    if n == 1:
      return d
    if n in memo:
      return memo[n]
    tmp = n * d
    if n % 2 == 0:
      tmp = min(tmp, a + solve(n//2))
    else:
      tmp =  min(tmp, a + d + solve(n//2), a + d + solve(n//2+1))
    if n % 3 == 0:
      tmp = min(tmp, b + solve(n//3))
    else:
      ret1 = n % 3
      ret2 = 3 - ret1
      tmp = min(tmp, b + d*ret1 + solve(n//3), b + d*ret2 + solve(n//3+1))
    if n % 5 == 0:
      tmp = min(tmp, c + solve(n//5))
    else:
      ret1 = n % 5
      ret2 = 5 - ret1
      tmp = min(tmp, c + d*ret1 + solve(n//5), c + d*ret2 + solve(n//5+1))
    memo[n] = tmp
    return memo[n]
    
  print(solve(N))

