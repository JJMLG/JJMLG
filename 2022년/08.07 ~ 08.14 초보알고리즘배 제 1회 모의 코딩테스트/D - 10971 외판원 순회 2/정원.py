def dfs(start, now):
    global result, tmp
    if tmp > result: return # 백트래킹
    for next in range(N): # 다음 방문 지점
        # 다음 방문할 지점이 지금 지점과 다르고
        # 방문한 적이 없으며
        # 방문을 할 수 있을 때(W배열에 값이 존재할 때)
        if now != next and not visited[next] and W[now][next]:
            visited[next] = 1 # 다음 지점 방문 찍고
            tmp += W[now][next] # 그 지점의 코스트를 더하고
            dfs(start, next) # 해당 지점 탐색
            visited[next] = 0 # 방문 지워주고
            tmp -= W[now][next] # 코스트 지워주고
        elif sum(visited) == N and W[now][start]:
            tmp += W[now][start] # 코스트 더하고
            if tmp < result: result = tmp # 최소값 갱신
            tmp -= W[now][start] # 코스트 지워주고

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
result = int(1e9) # 가상의 최소값
visited = [0] * N # 방문 배열
for n in range(N): # 모든 점에서 다 출발해본다
    tmp = 0 # 해당 출발의 임시 결과값
    visited[n] = 1 # 들어가면서 찍고
    dfs(n, n) # 출발 시, 시작점과 탐색점은 같다
    visited[n] = 0 # 나오면서 지운다
print(result) # 얻은 최소값 출력

"""
시간 : 80분(혼자 고민) + 10분("질문검색"탭에서 반례 및 힌트 참고)
풀이
    갈 수 있는 동선을 모두 체크하여(브루트포스)
    dfs로 탐색하면서
    방문배열을 만들어서, 들어갈 때 찍고, 나올 때 지워준다
    모든 점을 탐색했을 때 시작점으로 돌아가서
    해당 순회의 결과값이 최소값인지 비교하여 갱신한다
    (from itertools import permutation을 사용하여 풀 수도 있을 것이다)

    문제의 함정
        1. 다음 지점으로 갈 수 없는 경우가 있다
            순회 도중에 갈 수 없는 경우만 구현하였더니 오답이었고
            마지막 지점에서 다시 시작점으로 갈 수 없는 경우를 구현해주니 맞았음
        2. 순회 도중, 이미 구한 최소값보다 값이 커지면 return한다 (백트래킹)
"""