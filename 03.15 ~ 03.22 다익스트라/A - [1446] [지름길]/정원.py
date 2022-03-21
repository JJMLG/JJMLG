"""
세준이는 지름길을 타고 이동하지 않는다
그저 일자로 직진하면서
지름길이 있는지, 있다면 그 지름길을 지나갈 때
운전거리가 얼마나 줄어드는지"만" 확인한다
세준이는 일자로 간다
"""
from collections import deque
N, D = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(N)]
tmp.sort(key=lambda x:x[0]) # 출발점 기준 정렬
road = deque(tmp) # 지름길들을 담아놓음
# 문제의 조건 : D < 10000
dp = [int(1e4) for _ in range(D+1)] # 1e4 = 10000.0, 인덱스 위한 D+1
dp[0] = 0 # 시작은 0
for i in range(D): # i = 세준이 위치
    # 현재 위치에서 갈 수 있는 지름길이 있을 때
    while road and road[0][0] == i:
        x = road.popleft() # 지름길을 꺼내와서
        if x[1] > D: # 목적지를 넘어가면
            continue # 패스
        # 지름길의 끝에 거리 갱신
        dp[x[1]] = min(dp[i] + x[2], dp[x[1]])
        # print(i, x[1], x[2]) # 디버깅
        # print(dp) # 디버깅
    # 다음 칸의 거리는, 
    # min(이전 칸에서 한 칸 이동한 거리, 지름길 타고 넘어온 거리)
    dp[i+1] = min(dp[i] + 1, dp[i+1])
# print(dp) # 디버깅
# 세준이는 지름길을 타고 이동하지는 않았지만
# 일자로 이동하면서 파악한 지름길들을
# 적절히 활용하여 목적지에 도착할 수 있는 최소거리를
print(dp[D]) # 출력