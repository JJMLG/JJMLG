import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs():
    pass

n = int(input())
m = int(input())

city = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
# print(city)
# print(plan)

graph = [[] * (n+1) for _ in range(n+1)]
# print(graph)
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            graph[i+1].append(j+1)
            # graph[j+1].append(i+1)
print(graph)

for i in range(n):
    bfs(plan[i])


