s = input()
n = len(s)
news = []
for l in s:
  news.append(l)
s = news
for i in range(n):
  if s[i] == '?':
    s[i] = 'D'
print(''.join(s))

