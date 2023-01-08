import sys


from collections import deque
from pprint import pprint


def back(d):
    

    if d == 'U':
        return 'D'
    elif d == 'D':
        return 'U'
    elif d == 'L':
        return 'R'
    elif d == 'R':
        return 'L'
    

def search(x,y):
    up = 0
    down = 0
    left = 0
    right = 0
    for i in range(0,x):
        if arr[i][y] == -1:
            up += 1

    for i in range(0,y):
        if arr[x][i] == -1:
            left += 1

    for i in range(x+1,n):
        if arr[i][y] == -1:
            down += 1
    for i in range(y+1,n):
        if arr[x][i] == -1:
            right += 1
  
    maxx = max(up,down,left,right)
    if up ==maxx:
        return 'U'
    elif right == maxx:
        return 'R'
    elif down == maxx:
        return 'D'
    elif left == maxx:
        return 'L'


dx = [-1,1,0,0,0]
dy = [0,0,-1,1,0]

dict = {
    'U' : 0,
    'D' : 1,
    'L' : 2,
    'R' : 3,
    'S' : 4,
}
n = int(input())
arr = [[0]*n for _ in range(n)]
order = deque(input())
manX, manY = map(int,input().split())
manX -=1 
manY -= 1
w = int(input())
for i in range(w):
    x,y=map(int,input().split())
    x -= 1
    y -= 1
    arr[x][y] = -1
    
z = int(input())
queue = deque()
for i in range(z):
    x,y,g,d,v = input().split()
    x = int(x)
    y = int(y)
    g = int(g)
    v = int(v)
    x -= 1
    y -= 1
    queue.append((x,y,g,d,v))
day = int(input())


for ans in range(day):
    if order:
        o = order.popleft()
    
        nx = manX + dx[dict[o]]
        ny = manY + dy[dict[o]]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0:
                manX = nx
                manY = ny
   
    for i in range(len(queue)):

        x,y,g,d,v = queue.popleft()
        
        
        # print(x,y,g,d,v)
        flag = 0
        for j in range(v):
     
            nx = x + dx[dict[d]]
            ny = y + dy[dict[d]]
            if 0 <= nx < n and 0 <= ny < n:
                # 벽에 부딪힘
                if arr[nx][ny] == -1:
                    # 하급 좀비
                    if g == 0:
                        d = back(d)            
                        queue.append((x,y,g,d,v))
                        flag = 1
                        break
                    # 상급좀비
                    else:
                        arr[nx][ny] = 0                       
                        break
                        
                # 안붇지힘
                else:
                    x = nx
                    y = ny
            #경계
            else:
                if g == 0:
                    d = back(d)
                    queue.append((x,y,g,d,v))
                    flag = 1    
                    break
                # 상급좀비
                else:
                    break
        if flag == 0:
            if g == 1:
                d = search(x,y)                      
                queue.append((x,y,g,d,v))
                
            else:
                queue.append((x,y,g,d,v))
    
    for i in range(len(queue)):
        if queue[i][0] == manX and queue[i][1] == manY:
            print(ans+1)
            print('DEAD...')
            exit()
    
print('ALIVE!')

                  

    
