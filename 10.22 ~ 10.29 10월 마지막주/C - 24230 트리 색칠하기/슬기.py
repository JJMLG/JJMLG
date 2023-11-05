import sys
input = sys.stdin.readline

N = int(input())
color = list(map(int, input().rstrip().split()))
tree = [[] for _ in range(N)]
visited = [0 for _ in range(N)]

for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

coloring_times = 0
stack = []
stack.append(0)
visited[0] = 1

while stack:
    node = stack.pop()
    for near_node in tree[node]:
        if visited[near_node] == 0:
            visited[near_node] = 1
            if color[node] != color[near_node]:
                coloring_times += 1
            stack.append(near_node)

if color[0] != 0:
    coloring_times += 1

print(coloring_times)