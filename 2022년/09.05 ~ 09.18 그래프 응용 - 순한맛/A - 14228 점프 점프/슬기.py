import sys
sys.stdin = open('input.txt')

stone = int(input())
distance = list(map(int, input().split()))
start = int(input())

visited = [0] * stone

cnt = 1

def dfs(x):
    visited[x] = 1
    left = x - distance[x]
    right = x + distance[x]

    if left >= 0 and visited[left] == 0:
        dfs(left)
    if right < stone and visited[right] == 0:
        dfs(right)


dfs(start-1)
print(sum(visited))