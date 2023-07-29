from collections import deque

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    cnt = 0
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        #print(v, end=' ')
        cnt += 1
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt


def solution(n, wires):
    answer = n - 2 #  두 전력망이 갖게 되는 송전탑의 개수 차이의 절댓값 중 최댓값 (만약 n이 9일때 최대 절댓값은 두 전력망이 1과 8일때 즉 7이된다.)
    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for i in range(n+1)]
        visited = [False] * (n+1)
        tmps.pop(i) # i번째 전선 제거
        for wire in tmps:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
        for idx,g in enumerate(graph):
            if g != []: # n개의 송전탑 중 다른 송전탑과 연결된 송전탑을 시작점으로 지정
                start = idx
                break
        cnts = bfs(graph, start, visited) # bfs를 이용하여 시작점에서 다른 송전탑 탐색함. 이때 탐색 가능한 송전탑 개수를 cnts에 담음(이는 즉 연결된 송전탑의 개수임)
        other_cnts = n - cnts # 전력망을 둘로 나눌 때 첫번째 전력망 개수는 cnts이므로 나머지 전력망 개수는 n - cnts로 구한다.
        if abs(cnts - other_cnts) < answer:
            answer = abs(cnts - other_cnts)
    return answer