import sys
from collections import deque
from pprint import pprint


def sol():
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    a,b = map(int,input().split())
    # print(a,b)
    n,m =  map(int,input().split())
    arr = [[0]*a for _ in range(b)]
    direction = [[0,0,0] for _ in range(n+1)]
    for i in range(n):
        x,y,pos = input().split()
        # print(x,y)
        x = int(x)
        y= int(y)
        arr[b-y][x-1] = 1
        if pos == 'E':
            pos = 1
        elif pos == 'N':
            pos = 0
        elif pos == 'S':
            pos = 2
        elif pos == 'W':
            pos = 3
        direction[i+1] = [b-y,x-1,pos]


    for j in range(m):
        num,do,cnt = input().split()
        num = int(num)
        cnt = int(cnt)

    
        if do == 'L':
            direction[num][2] = (direction[num][2] - cnt) % 4
        elif do == 'R':
            direction[num][2] = (direction[num][2] + cnt) % 4
        elif do == 'F':
            
            while cnt > 0:
                nx = direction[num][0] + dx[direction[num][2]]
                ny = direction[num][1] + dy[direction[num][2]]
        
                if nx <0 or nx >= b or ny < 0 or ny >= a:
                    print(f'Robot {num} crashes into the wall')
                    return
                if arr[nx][ny] == 1:
                    for k in range(len(direction)):
                        if direction[k][0] == nx and direction[k][1] == ny:

                            print(f'Robot {num} crashes into robot {k}')
                            return
                
                
                arr[nx][ny] = 1
                arr[direction[num][0]][direction[num][1]] = 0
                direction[num][0] = nx
                direction[num][1] = ny


                cnt -= 1

        
    print("OK")


# t = int(input())
# for _ in range(t):
sol()
    