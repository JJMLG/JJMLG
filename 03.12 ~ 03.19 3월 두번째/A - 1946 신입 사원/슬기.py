import sys
sys.stdin = open('input.txt')

t = int(input())
for _ in range(t):
    n = int(input())
    scores = []

    for _ in range(n):
        grade, rank = map(int, input().split())
        scores.append([grade, rank])
    scores.sort(key=lambda x: (-x[0], x[1]))
    print(scores)
    cnt = 0
    # g_min = scores[-1][0]
    # r_min = scores[0][1]
    for i in range(n):
        for j in range(i, n):
            if scores[i][0] > scores[j][0]:
                if scores[i][1] < scores[j][1]:
                    cnt += 1
                    break
    print(cnt)