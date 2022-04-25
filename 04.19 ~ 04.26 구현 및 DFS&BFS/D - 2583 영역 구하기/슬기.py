import sys
sys.stdin = open('input.txt')

m, n, k = map(int, input().split())
# print(m, n , k)

paper = [[0] * (n+1) for _ in range(m+1)]
print(paper)

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    # print(x1, y1, x2, y2)
    for i in range(x2-x1+1):
        if paper[i][y1] == 0:
            paper[i][y1] += 1
        # for j in range(y2-y1+1):
        #     if paper[i][j] == 0:
        #         paper[i][j] += 1
print(paper)