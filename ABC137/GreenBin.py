char_num = int(input())
char_length = 10
chars = []
for i in range(char_num):
    chars.append(input())


class CharArrange:
    def __init__(self, char):
        self.char = char

    def run(self):
        self.char = self.char2OrdList(self.char)
        for pos in range(1, len(self.char)):
            self.insertSort(self.char, pos, self.char[pos])
        self.char = self.ordList2Str(self.char)

    def char2OrdList(self, char):
        return list(map(ord, char))

    def ordList2Str(self, ordList):
        return ''.join(list(map(chr, ordList)))

    def insertSort(self, A, pos, value):
        i = pos - 1
        while (i >= 0 and A[i] > value):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = value
        return A


for i, char in enumerate(chars):
    ca = CharArrange(char)
    ca.run()
    chars[i] = ca.char
