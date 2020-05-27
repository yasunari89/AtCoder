word_number, questions_number = map(int, input().split())
# words = list(input())
words = input()
questions = []
for question in range(questions_number):
    a,b = map(int, input().split())
    questions.append([a-1, b-1])

# 複数回の問題を2秒以内はきついので前処理する必要あり
# for i in range(len(questions)):
#     counter = 0
#     for j in range(questions[i][0], questions[i][1]):
#         # if words[j] == "A" and words[j+1] == "C":
#         if words[j: j+2] == "AC":
#             counter += 1
#     print(counter)

hasAC = [0] * word_number
for i in range(word_number-1):
    if words[i: i+2] == "AC":
        hasAC[i+1] = hasAC[i] + 1
    else:
        hasAC[i+1] = hasAC[i]

for i in range(questions_number):
    print(hasAC[questions[i][1]] - hasAC[questions[i][0]])
