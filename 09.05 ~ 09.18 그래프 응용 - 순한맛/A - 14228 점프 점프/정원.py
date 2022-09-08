from collections import deque

N = int(input())
arr = list(map(int, input().split()))
start = int(input()) - 1 # 인덱스 맞추기
visited = [0] * N # 점들의 방문 배열
Q = deque()
Q.append(start) # 시작점 넣고 출발
while Q:
    now = Q.popleft()
    if visited[now]: continue # 방문한 적 있는 점이면 continue
    visited[now] = 1 # 방문 처리
    tmp = arr[now] # 현재 지점에서 점프할 수 있는 거리
    front, back = now+tmp, now-tmp # 점프 시 인덱스
    if 0<=front<N and not visited[front]:
        Q.append(front) # 앞으로 점프
    if 0<=back<N and not visited[back]:
        Q.append(back) # 뒤로 점프
print(sum(visited)) # 방문한 적 있는 점들의 수 출력