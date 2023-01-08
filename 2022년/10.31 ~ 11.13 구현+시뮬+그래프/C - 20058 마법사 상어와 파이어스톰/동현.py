
import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')


n,q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2**n)]
temp = [[0]*(2**n) for _ in range(2**n)]
queue = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited_2 = [[0]*(2**n) for _ in range(2**n)]
def search(x,y):
    tmp = 0 
    
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0 <= nx < 2**n and 0 <= ny < 2**n and temp[nx][ny] >0:
            tmp += 1
    return tmp


def bfs(a,b):
    cnt = 0
    queue.append([a,b])
    while queue:
        x,y = queue.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 2**n and 0 <= ny < 2**n and arr[nx][ny] >0 and visited_2[nx][ny] == 0:
                queue.append([nx,ny])
                visited_2[nx][ny] = 1
                cnt += 1
    
    return cnt

def turn(size):
    # for k in range(0,8,2**size):
    #     print(k)
    global arr, temp
    visited = [[0]*(2**n) for _ in range(2**n)] 
    for i in range(0,2**n,2**size):
        for j in range(0,2**n,2**size):
            for q in range(i,i+2**size):
                for w in range(j,j+2**size):
                    temp[w-j+i][2**size-q-1+j+i] = arr[q][w]
    for i in range(2**n):
        for j in range(2**n):
        
            ice = search(i,j)
            if ice < 3:
                visited[i][j] = 1
    
    for i in range(2**n):
        for j in range(2**n):
            temp[i][j] -= visited[i][j]
                
    
    arr = [item[:] for item in temp]
    
    temp = [[0]*(2**n) for _ in range(2**n)]


l = list(map(int,input().split()))
for i in l:
    turn(i)
# pprint(arr)
ans_1 = 0
ans_2 = 0
for i in range(2**n):
    for j in range(2**n):
        
        
        if arr[i][j] > 0:
            ans_1 += arr[i][j]
            if visited_2[i][j] == 0:
                p = bfs(i,j)
                if p > ans_2:
                    ans_2 = p
            
print(ans_1)
print(ans_2)
# print(arr)

