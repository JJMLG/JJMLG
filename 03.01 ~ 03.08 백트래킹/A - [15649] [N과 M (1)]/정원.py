def dfs(x): # x는 숫자 고른 개수
    if x == M: # M개만큼 골랐으면
        print(*result) # 들어있는 순열 언패킹
        return # 해당 재귀 종료
    
    for i in range(N): # 재귀를 통해, N개중 하나 -> N-1개중 하나 -> N-2개중 하나 ...
        if visited[i]: # 이미 고른 수이면
            continue

        result.append(arr[i]) # 하나 고르고
        visited[i] = 1 # 방문처리 하고
        dfs(x+1) # 다음 숫자 고르기
        result.pop() # 돌아와서 골랐던 숫자 빼고
        visited[i] = 0 # 방문 취소하고


N, M = map(int, input().split())

arr = list(range(1, N+1))

visited = [0] * N

result = []

dfs(0) # 고른 숫자 0개부터 시작