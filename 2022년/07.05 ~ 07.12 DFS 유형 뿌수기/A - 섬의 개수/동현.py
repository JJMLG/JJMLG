import sys
sys.stdin=open('input.txt')


dx = [0,0,-1,1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]


def dfs(x,y,width,height):
    arr[x][y] = 0

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < height and 0 <= ny < width and arr[nx][ny] == 1:
            dfs(nx,ny,width,height)

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int,input().split())))

    cnt = 0
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                cnt += 1
                dfs(i,j,w,h)
    print(cnt)
