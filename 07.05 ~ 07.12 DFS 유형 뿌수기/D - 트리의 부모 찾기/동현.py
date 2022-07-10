import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline
n = int(input())
arr = [[]*(n+1) for _ in range(n+1)]
result = [0]*(n+1)
result[1] = 1
for i in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(start):
    for k in arr[start]:
      
        if result[k] == 0:
            result[k] = start
            dfs(k)
        


dfs(1)
for i in (result[2:]):
    print(i)