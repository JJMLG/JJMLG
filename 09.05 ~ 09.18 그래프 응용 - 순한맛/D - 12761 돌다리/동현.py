import sys
from collections import deque
import copy 

a,b,n,m = map(int,input().split())

# nx = [1,-1,a,-a,b,-b,]
queue = deque()
queue.append(n)
visited = [-1]*100001
visited[n] = 0
while queue:
    t= queue.popleft()
 
    if t == m:
        break
    for i in [1,-1,a,-a,b,-b,'a','b']:
     
        if i == 'a':
            if 0 < a*t < 100001 and (visited[a*t] == -1 or visited[a*t] > visited[t] +1) :
                queue.append(a*t)
                visited[a*t] = visited[t] + 1
        elif i == 'b':
            if 0 < b*t < 100001 and (visited[b*t] == -1 or visited[b*t] > visited[t] +1) :
                queue.append(b*t)
                visited[b*t] = visited[t] + 1
        else:
            
            if 0 < t+i < 100001 and (visited[t+i] == -1 or visited[t+i] > visited[t] +1) :
                queue.append(t+i)
                visited[t+i] = visited[t] + 1
    
print(visited[m])