char_num = int(input())
char_length = 10
chars = []
for i in range(char_num):
    chars.append(input())


class CharArrange:
    def __init__(self, char):
        self.char = char

    def char_run(self):
        list_char = self.str2ord_list(self.char)
        for pos in range(1, len(list_char)):
            self.insert_sort(list_char, pos, list_char[pos])
        self.char = self.ordList2Str(list_char)

    def order_run(self, chars):
        for i, char in enumerate(chars):
            chars[i] = self.ord_list2ord_concat(self.str2ord_list(char))
        for pos in range(len(chars)):
            self.insert_sort(chars, pos, chars[pos])
        self.ord_chars = chars

    def str2ord_list(self, char):
        return list(map(ord, char))

    def ordList2Str(self, ordList):
        return ''.join(list(map(chr, ordList)))

    def ord_list2ord_concat(self, ord_list):
        self.ord_concat = ''
        for ord_num in ord_list:
            self.ord_concat += str(ord_num)
        return int(self.ord_concat)

    def insert_sort(self, A, pos, value):
        i = pos - 1
        while (i >= 0 and A[i] > value):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = value
        return A


for i, char in enumerate(chars):
    CA = CharArrange(char)
    CA.char_run()
    chars[i] = CA.char
CA.order_run(chars)
ord_chars = CA.ord_chars

counter = 0
for i in range(len(ord_chars) - 1):
    k = i + 1
    while (ord_chars[i] == ord_chars[k]):
        counter += 1
        if k == len(ord_chars) - 1:
            break
        else:
            k += 1
print(counter)
