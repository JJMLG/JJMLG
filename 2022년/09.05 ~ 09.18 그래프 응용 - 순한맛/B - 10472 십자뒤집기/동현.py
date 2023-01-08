import sys
from collections import deque
import copy 


dx = [-1,1,0,0,0]
dy = [0,0,-1,1,0]
def bfs(arr):
    visited = [0]*513
    queue = deque()
    cnt2 = 0
    queue.append(arr)
    while queue:
        test = len(queue)
        for _ in range(test):
            t = queue.popleft()
            
            if t == target:
                return cnt2
                
            # print(t)
            
                
            for i in range(3):
                for j in range(3):
                    tCopy = [item[:] for item in t]
                    tos = check(tCopy,i,j)
                    vCode = visitCode(tos)
                    
                    if visited[vCode] == 0:
                        queue.append(tos)
                        visited[vCode] = 1
        cnt2 += 1

def visitCode(pos):
    code = ''
    for i in range(3):
        for j in range(3):
            if pos[i][j] == '*':
                code += '1'
            else:
                code += '0'
    return int(code,2)

def check(pos,x,y):
    for k in range(5):
        nx = x + dx[k]
        ny = y + dy[k]
        
        if 0 <= nx < 3 and 0 <= ny < 3:
            if pos[nx][ny] == '.':
                pos[nx][ny] = '*'
          
            else:
                pos[nx][ny] = '.'
    
   
    return pos

n = int(sys.stdin.readline())
for _ in range(n):
    target = [list(input()) for _ in range(3)]
    arr = [['.','.','.'] for _ in range(3)]
    
    
    answer = bfs(arr)
    print(answer)
    
    
        


    


    
    
