import sys
from collections import deque
sys.stdin = open('2583.txt')
M, N, K = map(int, input().split())
quadrangle = []
que = deque()
# 입력을 받고
# 기록하기 위한 array의 가로 세로 길이를 구하기 위해서
tempx = 0
tempy = 0
quadrangle = [list(map(int, input().split())) for _ in range(K)]
record = [[0] * N for _ in range(M)]

def bfs(cnt):
    while que:
        y, x = que.popleft()
        for i in range(4):
            dy = Y[i]+y
            dx = X[i]+x
            if dy >= M or dy <0 or dx >= N or dx < 0 or record[dy][dx] == 1:
                pass
            else:
                que.append([dy, dx])
                record[dy][dx] = 1
                cnt += 1
    if cnt != 0:
        return result.append(cnt)
    else:
        pass

for i in quadrangle:
    x = []
    y = []
    for j in range(4):
        if j % 2 == 0:
            x.append(i[j])
        else:
            y.append(i[j])
    for c in range(y[0], y[1]):
        for z in range(x[0], x[1]):
            record[c][z] = 1

Y = [-1, 0, 1, 0]
X = [0, 1, 0, -1]
result = []

for i in range(N):
    for j in range(M):
        que.append([j, i])
        bfs(0)
result = sorted(result)
print(len(result))
print(*result)

