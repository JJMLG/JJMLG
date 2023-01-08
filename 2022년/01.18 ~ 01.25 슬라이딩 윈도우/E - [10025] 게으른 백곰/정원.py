N, K = map(int, input().split())

pen = [0] * 1000001 # 우리(pen)의 범위

now = K # K에서 시작해야, 앞으로 K만큼, 뒤로 K만큼

x_max = 0 # 양동이좌표 최대까지만 탐색

for n in range(N):
    g, x = map(int, input().split())

    pen[x] = g # 우리 채우기

    if x > x_max:
        x_max = x # 최대 양동이좌표 저장

result = window = sum(pen[:now+K+1]) # 초기값

now += 1 # 한 칸 앞으로

# 백만 다 안돌고, 최대양동이까지만 탐색
while now+K <= x_max: 
    # 윈도우 한 칸 앞으로 슬라이딩~
    window -= pen[now-K-1]
    window += pen[now+K]
    
    # 최대값 갱신 가능한가?
    if window > result:
        result = window
    
    now += 1 # 한 칸 앞으로~

print(result)