import sys
sys.stdin = open('input.txt')

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
print(graph)