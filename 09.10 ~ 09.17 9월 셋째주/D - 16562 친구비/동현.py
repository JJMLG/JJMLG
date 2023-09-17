import sys
import heapq
from itertools import combinations
sys.stdin=open('input.txt')
sys.setrecursionlimit(10**9)

n,m,k = map(int,input().split())
ls = list(map(int,input().split()))
arr = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
result = []
def dfs(x, lst):
    visited[x] = 1
    for i in arr[x]:
        if visited[i] == 0:
            lst.append(i)
            dfs(i, lst)
    return lst

for i in range(m):
    v,w = map(int,input().split())
    # if v == w:
    #     arr[v].append(w)
    #     continue
    
    arr[v].append(w)
    arr[w].append(v)


for i in range(n):
    if visited[i] != 0 :
        one = dfs(i, [i])
        temp = 987654321
        for j in one:
            if temp > ls[j]:
                temp = ls[j]
        result.append(temp)

if sum(result) <= k:
    print(sum(result))
else:
    print('Oh no')