import sys
from queue import deque
queue = deque()
print(queue)
n,m = map(int, input().split())
pictures = [list(map(int, input().split())) for _ in range(n)]
record = [[0 for _ in range(m)] for _ in range(n)]
pictureNumber = 0
maxCnt = 0
cnt = 0
Y = [-1, 0, 1, 0]
X = [0, 1, 0, -1]

def bfs(y,x):
    global cnt
    queue.append([y,x])
    pictures[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            dy = y+Y[i]
            dx = x+X[i]
            if dy < 0 or dx < 0 or dx > m - 1 or dy > n - 1 or pictures[dy][dx] == 0:
                pass
            else:
                cnt += 1
                record[dy][dx] = cnt
                pictures[dy][dx] = 0
                queue.append([dy, dx])
for i in range(n):
    for j in range(m):
        if pictures[i][j] == 0:
            pass
        else:
            cnt = 1
            record[i][j]=cnt
            bfs(i, j)
            pictureNumber += 1
            if maxCnt < cnt:
                maxCnt = cnt
# print(record)
print(pictureNumber)
print(maxCnt)

# ------------------------------------------------------
# sys.setrecursionlimit(10**6)
# n,m = map(int, input().split())
# pictures = [list(map(int, input().split())) for _ in range(n)]
# # print(pictures)
# record = [[0 for _ in range(m)] for _ in range(n)]
# pictureNumber = 0
# maxCnt = 0
# cnt = 0
# Y = [-1, 0, 1, 0]
# X = [0, 1, 0, -1]
#
# def dfs(y,x):
#     if pictures[y][x]==0:
#         return
#     else:
#         global cnt
#         pictures[y][x]=0
#         record[y][x]=1
#         cnt += 1
#         for i in range(4):
#             dy = y+ Y[i]
#             dx = x+ X[i]
#             if dy<0 or dx<0 or dx>m-1 or dy>n-1 or pictures[dy][dx]==0:
#                 pass
#             else:
#                 dfs(dy, dx)
#
# for i in range(n):
#     for j in range(m):
#         if pictures[i][j] == 0:
#             pass
#         else:
#             cnt=0
#             dfs(i, j)
#             pictureNumber += 1
#             if maxCnt < cnt:
#                 maxCnt = cnt
# # print(record)
# print(pictureNumber)
# print(maxCnt)