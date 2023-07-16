import sys
sys.setrecursionlimit(10**5)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    
    def dfs(x,y):
        nonlocal temp
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                temp += int(maps[nx][ny])
                visited[nx][ny] = 1
                dfs(nx,ny)
    
    result = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                temp = int(maps[i][j])
                visited[i][j] = 1
                dfs(i,j)
                result.append(int(temp))
    if result == []:
        answer = result = [-1]
    else:
        answer = sorted(result)
    return answer