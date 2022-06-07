visited = [0 for _ in range(31)]
for _ in range(28):
    a = int(input())
    visited[a]=1
for i in range(1, len(visited)):
    if visited[i] ==0:
        print(i)