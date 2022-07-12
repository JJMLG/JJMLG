import sys
sys.stdin=open('input.txt')
n = int(input())
a, b = map(int, input().split())
m = int(input())
family = [ False for _ in range(n+1)]
cnt = 0
parent = 0
for _ in range(n):
    try:
        parent, son = map(int, input().split())
        family[son] = parent
    except:
        pass

def dfs(start):
    global cnt, parent
    if family[start]==False:
        parent = start
    else:
        cnt+=1
        dfs(family[start])
    return parent

if dfs(a) == dfs(b):
    print(cnt)
else:
    print(-1)