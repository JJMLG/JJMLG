from collections import deque
import sys


n, m, k, x = map(int, input().split() )
arr = [ [] for _ in range(n+1) ] # n+1 개의 row 생성 idx 맞추기 위해서 n+1 개 생성

for _ in range(m):
    a,b = map(int,  input().split() )
    arr[a].append(b)
    
distance = [-1] * (n+1)
distance[x] = 0    

q = deque([x])
while q:
    now = q.popleft()
    for next_node in arr[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
    
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)