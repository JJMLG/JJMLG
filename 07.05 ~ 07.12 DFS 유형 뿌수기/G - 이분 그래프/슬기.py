import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')
sys.stdin.readline

def dfs(x, group):
    # 방문한 노드에 그래프 할당
    visited[x] = group

    for j in g[x]:
        # 방문 안 했다면
        if visited[j] == 0:
            # 그룹값 -1로 주어 dfs돌기
            if not dfs(j, -group):
                return False
        # 현재 정점과 연결된 정점의 그룹값이 동일하면 false
        elif visited[j] == visited[x]:
            return False
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    g = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        point1, point2 = map(int, input().split())
        g[point1].append(point2)
        g[point2].append(point1)

    for i in range(1, v+1):
        # 방문한 정점 아니면 dfs 실행
        if visited[i] == 0:
            result = dfs(i, 1)
            if not result:
                break
    #
    # if result:
    #     print('YES')
    # else:
    #     print('NO')
    print('YES' if result else 'NO')
