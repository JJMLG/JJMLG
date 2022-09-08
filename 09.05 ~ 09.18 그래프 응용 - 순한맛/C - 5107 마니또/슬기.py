import sys
sys.stdin = open('input.txt')


def dfs(v):
    global check
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = True
            check += 1

case = 1

while True:
    n = int(input())

    if n == 0:
        break

    graph = [[] for _ in range(n+1)]
    manitto = []
    name = {}
    cnt = 1
    answer = 0

    for _ in range(n):
        first_name, second_name = input().split()
        manitto.append([first_name, second_name])
        if first_name not in name.keys():
            name[first_name] = cnt
            cnt += 1
        if second_name not in name.keys():
            name[second_name] = cnt
            cnt += 1

    for a, b in manitto:
        x = name.get(a)
        y = name.get(b)
        graph[x].append(y)

    result = []
    for i in range(1, n+1):
        if i in result:
            continue
        check = 1
        visited = [0] * (n+1)
        dfs(i)
        if check == visited.count(True):
            for i in range(len(visited)):
                if visited[i] == True:
                    if i not in result:
                        result.append(i)
            answer += 1
    print('{} {}'.format(case, answer))

    case += 1