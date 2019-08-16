def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    current_max = max(A[1:N])
    current_max_index = A.index(current_max)
    print(current_max)
    previous_max = current_max
    previous_max_index = current_max_index
    for i in range(1, N):
        if i != previous_max_index:
            current_max = max([A[i-1], previous_max])
            current_max_index = previous_max_index
        else:
            current_max = max(A[0:i] + A[i+1:N])
            current_max_index = A.index(current_max)
        print(current_max)
        previous_max = current_max
        previous_max_index = current_max_index


if __name__ == '__main__':
    main()
