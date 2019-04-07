T = int(input())
N, P, lyndia_paths = [], [], []
for t in range(T):
    n = int(input())
    p = input()
    lyndia_paths.append([n, p])

for path in lyndia_paths:
    n, p = path[0], path[1]
    if p[-1] == 'S':
        p += 'E'
    else:
        p += 'S'
    initial_alphabet = p[0]
    arranged_input = initial_alphabet
    counter = 1
    for i in range(2*n-2):
        if p[i+1] == initial_alphabet:
            counter += 1
        else:
            arranged_input += str(counter)
            if initial_alphabet == 'S':
                initial_alphabet = 'E'
            else:
                initial_alphabet = 'S'
            arranged_input += initial_alphabet
            counter = 1
    arranged_input = arranged_input[:-1]

    if n % 2 == 0:
        output = ''
        for i in range(int(n / 2)):
            pair = arranged_input[4*i:4*(i+1)]
            for _ in range(int(pair[3])):
                output += pair[2]
            for _ in range(int(pair[1])):
                output += pair[0]
    else:
        output = ''
        for i in range(int((n - 1) / 2)):
            pair = arranged_input[4*i:4*(i+1)]
            for _ in range(int(pair[3])):
                output += pair[2]
            for _ in range(int(pair[1])):
                output += pair[0]
        if arranged_input[-2] == 'S':
            for _ in range(int(arranged_input[-1])):
                output += 'E'
        else:
            for _ in range(int(arranged_input[-1])):
                output += 'S'

    print(output)




            
