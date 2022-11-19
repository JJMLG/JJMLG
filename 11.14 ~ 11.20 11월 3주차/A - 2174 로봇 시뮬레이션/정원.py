import sys

input = sys.stdin.readline

direction_to_index = { # NESW를 0123으로 바꿔서 델타이동을 아래와 같이 할 것
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

A, B = map(int, input().rstrip().split())
arr = [[-1]*A for _ in range(B)]
N, M = map(int, input().rstrip().split())
robot_location = [(0, 0) for _ in range(N+1)] # n번 로봇의 좌표를 (y,x)꼴로 담을 배열 공간 N+1개만큼 생성
for n in range(1, N+1):
    x, y, direction = input().rstrip().split()
    # 예제처럼 왼쪽아래를 1,1로 두기 위해 아래와 같이 y좌표를 바꿔서 집어넣는다
    x, y, direction = int(x)-1, B-(int(y)), direction_to_index[direction]
    robot = n # 로봇 번호
    arr[y][x] = direction # 원본 배열에는 로봇이 바라보는 방향을 집어넣는다
    robot_location[robot] = (y, x)
# 디버깅
# for a in arr: print(a) 
# print()
orders = [] # 입력은 일단 다 받기 위해 리스트 생성
for m in range(M):
    robot, command, loop = input().rstrip().split()
    robot, loop = int(robot), int(loop)
    orders.append((robot, command, loop))
result = 'OK' # 명령들을 이상없이 수행하면 출력할 OK
for order in orders:
    if result != 'OK': break # 뭔가 심상치 않은 일이 생긴거야~
    robot, command, loop = order # ex) 1 F 3
    y, x = robot_location[robot] # 명령으로 들어온 로봇이 현재 배열에 위치한 좌표 y, x
    direction = arr[y][x] # 로봇이 보고 있는 방향
    if command == 'R': # 오른쪽으로 돌리고~
        arr[y][x] += loop
        arr[y][x] %= 4
    elif command == 'L': # 왼쪽으로 돌리고~
        for i in range(loop):
            arr[y][x] = (arr[y][x]+3)%4 # 오른쪽으로 세 번 돌린 것과 같다
    else: # 앞으로 가자!
        for i in range(loop):
            if result != 'OK': break # 뭔가 심상치 않은 일이 생긴거야~
            ny, nx = y+dy[direction], x+dx[direction] # 로봇의 다음 이동할 좌표
            if not (0<=ny<B) or not (0<=nx<A): # 벽에 부딪혔다 == 범위를 벗어났다
                result = f'Robot {robot} crashes into the wall'
            elif arr[ny][nx] != -1: # 다른 로봇과 부딪혔다
                crashed_robot = 0 # 부딪힌 로봇의 번호 초기화
                for n in range(N+1): # 부딧힌 로봇의 번호를 찾자
                    if robot_location[n] == (ny, nx): # 로봇들 중 ny,nx에 위치한 로봇의 인덱스
                        crashed_robot = n
                result = f'Robot {robot} crashes into robot {crashed_robot}'
            else: # 이상없이 앞으로 갈 수 있다
                arr[y][x], arr[ny][nx] = arr[ny][nx], arr[y][x] # 한 칸 앞으로
                y, x = ny, nx # 로봇의 새 좌표로 갱신
                robot_location[robot] = (y, x) # 로봇 좌표모음 배열도 갱신
    # 디버깅
    # for a in arr: print(a)
    # print()
print(result)