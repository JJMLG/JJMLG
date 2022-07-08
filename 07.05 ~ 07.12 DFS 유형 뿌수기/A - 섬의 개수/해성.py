w, h = map(int, input().split())
# print(w, h)
maps = [list(map(int, input().split())) for _ in range(h)]
# print(maps)
visited = [[0 for _ in range(w)] for _ in range(h)]
Y = [-1, -1, 0, 1, 1, 1, 0, -1]
X = [0, 1, 1 ,1 ,0 ,-1, -1, -1]
numberOfLand = 0
isLand = False
def dfs(y,x, isLand):
    if maps[y][x] != 1:
        return isLand
    # if isLand == True:
    for d in range(8):
        dy = Y[d]+y
        dx = x[d]+x
        if dy<0 or dy>h-1 or dx <0 or dx > w-1 or visited[dy][dx]==1:
            pass
        else:
            visited[dy][dx] = 1
            dfs(dy,dx, True)


for i in range(h):
    for j in range(w):
        # 만약 시작지점이 0이아니라면 dfs돌리기
        if maps[i][j] !=0 and visited[i][j] ==0:
            dfs(i,j, False)
            if isLand == True:
                numberOfLand+=1
                isLand = False
            else:
                pass


