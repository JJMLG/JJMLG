from collections import deque

def solution(x, y, n):
    if x==y:
        return 0
    answer = 0
    queue = deque()
    queue.append(x)
    visited = [0] * (y+1 )
    while queue:
        
        t = queue.popleft()
        for i in (t+n,t*2,t*3):
            if i > y:
                continue
            if visited[i]:
                continue
            queue.append(i)
            visited[i] = visited[t] + 1
    
    if visited[y] == 0:
        answer = -1
    else:
        answer = visited[y]
    
    
    return answer