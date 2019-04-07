times = int(input())
input_numbers = [int(input()) for _ in range(times)]

for case in range(times):
    input_number = input_numbers[case]
    digit = len(str(input_number))
    separate = 0
    for i, number in enumerate(str(input_number)):
        number = int(number)
        if number == 4:
            separate += float(1 * 10**(digit-i-1))
    print('Case#{0}: {1} {2}'.format(case+1, int(separate), int(input_number-separate)))
