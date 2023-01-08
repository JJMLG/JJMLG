import sys

input = sys.stdin.readline
INF = int(1e9) # 가상의, 변경해야 할 길의 수 최대값

N, M = map(int, input().rstrip().split())
arr = [[INF]*N for _ in range(N)]
for m in range(M):
    u, v, b = map(int, input().rstrip().split())
    u, v = u-1, v-1 # 인덱스 맞추기
    if b == 0: # 일방통행이면
        arr[u][v] = 0 # 한 쪽은 괜찮지만
        arr[v][u] = 1 # 다른 한 쪽은 길을 바꿔줘야 함
    else: arr[u][v], arr[v][u] = 0, 0 # 양방향 통행이면 서로 오갈 수 있음
for k in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], arr[a][k]+arr[k][b]) # 최소값(기존에 구한 변경해야 하는 길의 수, 새로 구한 변경해야 하는 길의 수)
K = int(input().rstrip())
for k in range(K):
    s, e = map(int, input().rstrip().split())
    s, e = s-1, e-1 # 인덱스 맞추기
    if s == e: print(0) # 1->1 같은 경우는 갔다 돌아오는 것이 아닌, 출발 자체를 하지 않는 것으로 함
    else: print(arr[s][e])

# https://www.acmicpc.net/problem/11562
""" 
플로이드-워셜 알고리즘
a->b 로 가기 위해 바꿔야하는 일방통행 길의 수는
a->k->b 로 가기 위해 바꿔야 하는 길의 수와 같다
"""