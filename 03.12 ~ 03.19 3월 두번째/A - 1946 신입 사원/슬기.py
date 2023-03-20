import sys
sys.stdin = open('input.txt')

t = int(input())
for _ in range(t):
    n = int(input())
    scores = []

    for _ in range(n):
        grade, rank = map(int, input().split())
        scores.append([grade, rank])
    scores.sort()
    # print(scores)
    cnt = 0

    tmp = scores[0][1]
    for i in range(n):
        if scores[i][1] > tmp:
            cnt += 1
        else:
            tmp = scores[i][1]
    print(n - cnt)