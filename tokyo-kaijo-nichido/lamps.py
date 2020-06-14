n, k = map(int, input().split())
brightness = list(map(int, input().split()))

for _ in range(k):
  zeros = [0 for _ in range(n)]
  for i, b in enumerate(brightness):
    left = max(0, i-b)
    right = min(n-1, i+b)
    for j in range(left, right+1):
      zeros[j] += 1
  brightness = zeros

brightness = [str(b) for b in brightness]
print(" ".join(brightness))

