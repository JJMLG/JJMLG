import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
poketmon = []
quiz = []

for _ in range(n):
    poketmon.append(input())

for _ in range(m):
    quiz.append((input()))
# print(quiz)

for i in range(m):
    if quiz[i].isdigit():
        quiz_num = int(quiz[i])
        print(poketmon[quiz_num-1])
    else:
        print(poketmon.index(quiz[i])+1)
