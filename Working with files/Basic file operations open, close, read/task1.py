import os

file = open('numberes.txt', 'r')

answer = []
for i in file:
    print(i, end='')
    answer.append(int(i))
    print()
answerr = sum(answer)
file.close()

answer_for = open('answer.txt', 'w')
answer_for.write(str(answerr))
answer_for.close()