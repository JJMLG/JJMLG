from collections import deque
import sys


a,b = map(int,input().split())
ans = 0

def dfs(s):
    global ans
    if s > b: return
    if s >= a: ans += 1
    dfs(s*10+4)
    dfs(s*10+7)

dfs(4)
dfs(7)
print(ans)
