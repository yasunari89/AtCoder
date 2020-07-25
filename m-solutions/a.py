x = int(input())
rank = {
    600: 8,
    800: 7,
    1000: 6,
    1200: 5,
    1400: 4,
    1600: 3,
    1800: 2,
    2000: 1
}

for p, r in rank.items():
    if p-200 <= x < p:
        print(r)