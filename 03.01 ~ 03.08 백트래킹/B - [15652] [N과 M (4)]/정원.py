def dfs(s, depth):
    global N, M

    if depth == M: # M개의 수를 담았을 때
        print(*result[1:]) # *로 언패킹해서 출력
        return # 재귀 탈출

    # 아직 M개의 수를 담지 않았을 때
    depth += 1 # 하나 더 고르자

    for i in range(s, N+1): # 시작하는 수 s부터 N까지
        result[depth] = i # depth번째 수는 i
        dfs(s, depth) # 한 depth더 들어가기
        s += 1 # 들어갔다 나왔으면 s를 하나 올리기


N, M = map(int, input().split())

result = [0] * (M+1) # 인덱스 맞추기 위한 M+1

dfs(1, 0) # 시작은 1, 깊이는 0부터 시작