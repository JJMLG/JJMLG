import sys
sys.setrecursionlimit(99999)
input = sys.stdin.readline
sys.stdin = open('input.txt')


def dfs(start, G, Parents):
    for i in G[start]:
        # 부모 입력해주기
        if Parents[i] == 0:
            Parents[i] = start
            dfs(i, G, Parents)

n = int(input())

# 트리 만들어주기
G = [[] for _ in range(n+1)]

# 부모 노드 저장
parents = [0 for _ in range(n+1)]
# print(parents)

for _ in range(n-1):
    point1, point2 = map(int, input().split())
    # 그래프 만들어주고, 연결 되는 점들 같이 append
    G[point1].append(point2)
    G[point2].append(point1)
    # print(G)

dfs(1, G, parents)

# 2부터 한 이유는 2번 정점 부터의 부모 노드를 출력하기 위해 1번이 루트임
for j in range(2, n+1):
    print(parents[j])