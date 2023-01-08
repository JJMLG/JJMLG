"""
반시계
11001110
-1
10011101

시계
11001110
1
01100111
"""

from pprint import pprint


def clockwise(i): # 시계방향
    global gears, visited
    if i not in range(4): # 톱니 인덱스가 범위를 벗어나면
        return # 함수 종료
    # print("clockwise!", i+1) # 디버깅
    try:
        if gears[i][2] != gears[i+1][6]: # 현재 톱니바퀴의 오른쪽 톱니바퀴와 극이 다르면
            visited[i] = 1 # 방문처리
            if not visited[i+1]: # 확인하지 않은 톱니바퀴에 대해
                counter_clockwise(i+1) # 오른쪽 톱니 반시계방향
    except:
        pass
    try:
        if gears[i][6] != gears[i-1][2]: # 현재 톱니바퀴의 왼쪽 톱니바퀴와 극이 다르면
            visited[i] = 1
            if not visited[i-1]:
                counter_clockwise(i-1) # 왼쪽 톱니 반시계방향
    except:
        pass
    tmp = [gears[i][-1]] + gears[i][:7] # 시계방향으로 돌려주기
    gears[i] = tmp

def counter_clockwise(i): # 반시계방향
    global gears, visited
    if i not in range(4): # 톱니 인덱스가 범위를 벗어나면
        return # 함수 종료
    # print('counter!!', i+1) # 디버깅
    try:
        if gears[i][2] != gears[i+1][6]: # 오른쪽 톱니와 극이 다르면
            visited[i] = 1
            if not visited[i+1]:
                clockwise(i+1) # 오른쪽 톱니 시계방향
    except:
        pass
    try:
        if gears[i][6] != gears[i-1][2]: # 왼쪽 톱니와 극이 다르면
            visited[i] = 1
            if not visited[i-1]:
                clockwise(i-1) # 왼쪽 톱니 시계방향
    except:
        pass
    tmp = gears[i][1:] + [gears[i][0]] # 반시계방향으로 돌려주기
    gears[i] = tmp


# 값들 입력받기
gears = [] # 톱니들
for _ in range(4):
    gears.append(list(map(int, input())))
K = int(input())
orders = [] # 돌리는 톱니번호와 방향들
for k in range(K):
    orders.append(tuple(map(int, input().split())))

# pprint(gears) # 디버깅

for order in orders:    
    # print(order) # 디버깅
    visited = [0] * 4 # 매 톱니마다 방문배열 초기화
    if order[1] == 1:
        clockwise(order[0]-1) # 시계방향
    elif order[1] == -1:
        counter_clockwise(order[0]-1) # 반시계방향
    # pprint(gears) # 디버깅

result = 0 # 결과값 초기화
num = 1 # 결과값에 더할 변수값 초기화
for i in range(4):
    if gears[i][0]: # 12시 톱니가 1이면
        result += num # 결과값 갱신
    num *= 2 # 1 2 4 8 

print(result) # 결과값 출력