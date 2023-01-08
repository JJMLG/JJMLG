import sys
sys.setrecursionlimit(10**6)
def dfs(y,x):
    if maps[y][x] != 1:
        return numberOfLand
    # if isLand == True:
    else:
        for d in range(8):
            dy = Y[d]+y
            dx = X[d]+x
            if dy<0 or dy>h-1 or dx <0 or dx > w-1 or visited[dy][dx]==1:
                pass
            else:
                visited[dy][dx] = 1
                dfs(dy,dx)
while True:
    w, h = map(int, input().split())
    if w ==0 and h ==0:
        break
    else:
    # print(w, h)
        maps = [list(map(int, input().split())) for _ in range(h)]
        # print(maps)
        visited = [[0 for _ in range(w)] for _ in range(h)]
        Y = [-1, -1, 0, 1, 1, 1, 0, -1]
        X = [0, 1, 1 ,1 ,0 ,-1, -1, -1]
        numberOfLand = 0

        for i in range(h):
            for j in range(w):
                # 만약 시작지점이 0이아니라면 dfs돌리기
                if maps[i][j] !=0 and visited[i][j] ==0:
                    numberOfLand += 1
                    dfs(i,j)
        print(numberOfLand)

