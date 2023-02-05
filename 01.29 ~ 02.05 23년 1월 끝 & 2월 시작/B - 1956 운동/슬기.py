import sys
sys.stdin = open('input.txt')


INF = int(1e9)

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
cnt = 0
visited = [INF] * (v+1)
# print(visited)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
