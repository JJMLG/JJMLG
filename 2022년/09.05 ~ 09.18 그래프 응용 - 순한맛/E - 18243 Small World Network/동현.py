import sys
from collections import deque
import copy 


def dfs(start,depth):
 
    visited[start] = depth
    for w in arr[start]:
        if visited[w] == -1 or visited[w] > visited[start] +1 :
            dfs(w,depth+1)
            
n,k = map(int,input().split())
arr = [[]*(n+1) for _ in range(n+1)]
for i in range(k):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)


flag = 0
for i in range(1,n+1):
    visited = [-1]*(n+1)
    dfs(i,0)

    
    if max(visited) > 6 or -1 in visited[1:]:
        flag = 1
        break
        

if flag == 0:
    print("Small World!")
else:
    print("Big World!")