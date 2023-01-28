import sys
# sys.stdin = open("input.txt")

def DFS(node):
    visit[node]=1
    for nnode in adjlist[node]:
        if(visit[nnode]): continue
        DFS(nnode)

def checkVisit():
    for n in range(M):
        if not visit[routes[n]]:
            return 0
    return 1

N = int(input())
M = int(input())
adjlist = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

for node in range(1, N+1):
    arr = list(map(int, input().split()))
    for nn in range(len(arr)):
        if(arr[nn]):
            adjlist[node].append(nn+1)
routes = list(map(int, input().split()))

DFS(routes[0])
ret = checkVisit()
if(ret):
    print("YES")
else:
    print("NO")