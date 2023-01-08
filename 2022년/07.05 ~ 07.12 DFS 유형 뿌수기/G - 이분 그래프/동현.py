import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def dfs(start,color):
    global tmp
    visited[start] = color
    for k in arr[start]:
        if visited[k] == color:
            tmp = False
            return
        if visited[k] == 0:
            dfs(k,color*-1)

t = int(input())
for tc in range(t):
    v,e = map(int,input().split())
    arr = [[]*(v+1) for _ in range(v+1)]
    visited = [0]*(v+1)
    tmp = True
    for _ in range(e):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    
    for i in range(1,v+1):
        if visited[i] == 0:
            dfs(i,1)
            if tmp == False:
                break
    
    if tmp:
        print('YES')
    else:
        print('NO')
    

    