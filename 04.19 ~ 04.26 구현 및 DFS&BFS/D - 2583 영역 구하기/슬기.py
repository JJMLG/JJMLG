import sys
sys.stdin = open('input.txt')


m, n, k = map(int, input().split())
# print(m, n , k)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

square = []

paper = [[0] * n for _ in range(m)]
# print(paper)

# 네모 채우기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        # print(i)
        for j in range(x1, x2):
            paper[i][j] = 1
# print(paper)

for u in range(m):
    for l in range(n):
        if paper[u][l] == 0:
            count = 1
            paper[u][l] = 1
            queue = [[u, l]]
            while queue:
                x, y = queue[0][0], queue[0][1]
                del queue[0]
                for a in range(4):
                    x1 = x + dx[a]
                    y1 = y + dy[a]
                    if 0 <= x1 < m and 0 <= y1 < n and paper[x1][y1] == 0:
                        paper[x1][y1] = 1
                        count += 1
                        queue.append([x1, y1])
            square.append(count)
print(len(square))
square.sort()
for z in square:
    print(z, end=' ')