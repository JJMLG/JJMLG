import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
t = int(input())

def dfs(start,tmp):
    global result
    visited[start] = 1
    tmp.append(start)

    if visited[ls[start]] == 1:
        if ls[start] in tmp: 
            for i in range(len(tmp)):
                if tmp[i] == ls[start]:
                    result += len(tmp[i:])
            return
        else:
            return
    else:
        dfs(ls[start],tmp)
for _ in range(t):
    n = int(input())
    ls = [0]+list(map(int,input().split()))

    visited = [0]*(n+1)

    result = 0
    for i in range(1,n+1):
        if visited[i] == 0:

            dfs(i,[])

    print(n-result)



