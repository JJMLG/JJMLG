import sys

n,m = map(int, input().split())
 
s = []
 
def dfs(i):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for j in range(1, n+1): 
        s.append(j)
        dfs(j)
        s.pop()
    
dfs(1)          