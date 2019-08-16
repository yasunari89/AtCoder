def main():
    L, R = map(int, input().split())
    if R - L >= 2019:
        print(0)
    else:
        left_rest = L % 2019
        right_rest = R % 2019
        start = min(left_rest, right_rest)
        last = max(left_rest, right_rest)
        rest_list = list(range(start, last+1))

        ans = 100000
        for i in range(len(rest_list)-1):
            ans = min(
                ans,
                (rest_list[i] * rest_list[i+1]) % 2019
            )
        ans = min(
            ans,
            (rest_list[-1] * rest_list[0]) % 2019
        )
        print(ans)


if __name__ == "__main__":
    main()
