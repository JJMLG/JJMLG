import sys
sys.stdin=open('input.txt')
sys.setrecursionlimit(10**6)
T = int(input())
def dfs(start):
    global cnt, now
    if now == start:
        return
    else:
        if visited[start] == 1:
            pass
        else:
            visited[start] = 1
            now = start
            dfs(numbers[start-1])
    # return now

for tc in range(T):
    N = int(input())
    idxList = list(range(N + 1))
    numbers = list(map(int, input().split()))
    cnt = 0
    now = 0
    visited = [0] * (N+1)

    for i in range(1,len(idxList)):
        if visited[i] == 1:
            pass
        else:
            dfs(i)
            cnt += 1
    print(cnt)

