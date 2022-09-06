import sys
sys.stdin = open('input.txt')

stone = int(input())
distance = list(map(int, input().split()))
start = int(input())

visited = [0] * stone

cnt = 1

def dfs(s):
    global visited, cnt

    for nx in (s+distance[s], s-distance[s]):
        if 0 <= nx < stone and visited[nx] == 0:
            cnt += 1
            visited[nx] = 1
            dfs(nx)

dfs(start-1)
print(cnt)