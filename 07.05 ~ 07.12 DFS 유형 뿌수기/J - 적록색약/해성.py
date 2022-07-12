import sys, copy
sys.stdin=open('input.txt')
sys.setrecursionlimit(10**6)
N = int(input())
colors = [list(input()) for _ in range(N)]
colorsN = copy.deepcopy(colors)
colorsY = copy.deepcopy(colors)
for i in range(N):
    for j in range(N):
        if colorsN[i][j] =='G':
            colorsN[i][j] = 'R'
resultN = 0
resultY = 0
Y = [-1, 0, 1, 0]
X = [0, 1, 0, -1]
# result1 = {'R':0, 'G':0, 'B':0}
# result2 = {'R':0, 'G':0, 'B':0}
def dfsY(y, x, now):
    now = colorsY[y][x]
    colorsY[y][x] = 0
    for i in range(4):
        dy = y + Y[i]
        dx = x + X[i]
        if dy < 0 or dx < 0 or dx > N-1 or dy > N-1 or colorsY[dy][dx] == 0 or colorsY[dy][dx] != now:
            pass
        else:
            dfsY(dy, dx, now)
def dfsN(y, x, now):
    now = colorsN[y][x]
    colorsN[y][x] = 0
    for i in range(4):
        dy = y + Y[i]
        dx = x + X[i]
        if dy < 0 or dx < 0 or dx > N - 1 or dy > N - 1 or colorsN[dy][dx] !=now:
            pass
        else:
            dfsN(dy,dx,now)
            # if now == 'B':
            #     if colorsN[dy][dx] == 'R' or colorsN[dy][dx] == 'G':
            #         pass
            # if now == 'R' or now == 'G':
            #     if colorsN[dy][dx] == 'B':
            #         pass
            # if now == 'R' and colorsN[dy][dx]=='G':
            #     dfsN(dy, dx, now)
            # if now =='G' and colorsN[dy][dx] =='R':
            #     dfsN(dy, dx, now)
            # if now == colorsN:
            #     dfsN(dy, dx, now)

# print(colorsY)
# print(colorsN)
for i in range(N):
    for j in range(N):
        if colorsY[i][j]:
            now = colorsY[i][j]
            dfsY(i, j, now)
            resultY += 1
# print(colorsY)
# print(colorsN)
for i in range(N):
    for j in range(N):
        if colorsN[i][j]:
            # print(11)
            now = colorsN[i][j]
            dfsN(i,j, now)
            resultN += 1
            # print(depth)
print(resultY)
print(resultN)


