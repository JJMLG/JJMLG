import sys
sys.stdin = open('input.txt')

stone = int(input())
distance = list(map(int, input().split()))
start = int(input())

visited = [0] + [0] * stone


def dfs(graph, s):
    jump = graph[s]

    if visited[s+1] == 0:
        visited[s+1] = 1

    



# for i in range(1, len(distance)+1):
#     if visited[start] == 0:
#         visited[start] = 1
#         dfs(distance, start)