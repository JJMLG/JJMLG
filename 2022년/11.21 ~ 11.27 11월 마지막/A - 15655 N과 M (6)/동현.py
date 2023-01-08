import sys

n, m = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
visited = [0]*10001
result = []
def dfs(start,lst):
    
    if len(lst) == m:
        result.append(lst[:])
        return

    for i in range(start,n):
        lst.append(ls[i])
        dfs(i+1,lst)
        lst.pop()


dfs(0,[])
for i in range(len(result)):
    print(*result[i])