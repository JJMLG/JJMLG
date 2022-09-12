INF = int(1e9)
N, K = map(int, input().split())
world = [[INF]*N for _ in range(N)] # 친구간 거리 배열 초기화
for k in range(K):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    world[A][B], world[B][A] = 1, 1 # 친구인 관계는 서로 거리가 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j: # 자기 자신과 친구는 카운트하지 않음
                world[i][j] = min(world[i][j], world[i][k]+world[k][j])
result = 'Small World!' # 초기값을 Small World로 놓고 거리가 6을 초과하는 관계를 찾을 것
for i in range(N):
    if result != 'Small World!': # Small World가 아닌 것이 증명되었다면 
        break
    for j in range(N):
        if i != j: # 자기 자신이 아니면서
            if world[i][j] > 6: # 친구 거리가 6을 초과한다?
                result = 'Big World!'
                break
print(result)

"""
플로이드 워셜(Floyd-Warshall) 알고리즘
https://velog.io/@kimdukbae/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Floyd-Warshall-Algorithm
i에서 j로 가는 최소값은
이미 구한 "i에서 j로 가는 값"과
"지점 k를 거쳐가는 i -> k -> j로 가는 값"
두 값중 최소값이다
"""

# https://www.acmicpc.net/problem/18243