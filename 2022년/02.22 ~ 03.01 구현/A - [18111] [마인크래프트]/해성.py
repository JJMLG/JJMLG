import sys
sys.stdin = open("18111.txt")

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
minn = 257
maxx = 0
temp = []
temp_b = B
result = []
# print(ground)
# 우선 땅을 고르기 위해 땅 높이가 될 수 있는 범위 찾기
for i in range(N):
    if maxx <= max(ground[i]):
        maxx = max(ground[i])
    if minn >= min(ground[i]):
        minn = min(ground[i])
# 땅 높이가 될 수 있는 범위
# print(minn, maxx)
try_list = list(range(minn, maxx+1))
# print(try_list)

# 땅을 고르는데 걸리는 최소 시간 찾아야하니까 min_time을 가장 오래걸릴 수 있는 시간으로 할당
temp_time = 0
min_time = (500*500)**2

for x in try_list:
    temp_b = B
    temp_time = 0
    for i in range(N):
        # 최소 시간보다 이미 넘겨버렸다면 그만하고 다음 후보로
        if temp_time > min_time:
            break
        for j in range(M):
            if x > ground[i][j]:
                temp_time += (x - ground[i][j])
                temp_b -= (x - ground[i][j])
            # 골라야할 땅 높이보다 크다면 블록 제거하는 시간 2초 더하고, 블록 인벤토리에 추가
            elif x < ground[i][j]:
                temp_time += (ground[i][j] - x) *2
                temp_b += (ground[i][j]-x)
    # 다했는데 인벤토리에 남은 블록이 0보다 작으면 불가능한 경우
    if temp_b < 0:
        pass
    else:
        # 다 계산하고 걸린 시간 최소시간으로 할당
        if temp_time < min_time:
            min_time = temp_time
            result.append([min_time, x])
        else:
            pass

result.sort()
print(*result[0])
#