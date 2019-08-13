A, B, C = map(int, input().split())
rest: int = C - (A - B)
result: int = (rest if rest >= 0 else 0)
print(result)
