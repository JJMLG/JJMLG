DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]
cube = { 'u': 1, 'f': 2, 'r': 3 }
cubeNum = [0] * 7    # 주사위 각 면에 적힌 숫자


def moveCube(direc):
    u = cube['u']; f = cube['f']; r = cube['r'];
    if direc == 0:
        cube['r'] = u; cube['u'] = 7 - r
    elif direc == 1:
        cube['u'] = r; cube['r'] = 7 - u
    elif direc == 2:
        cube['u'] = f; cube['f'] = 7 - u
    else:
        cube['f'] = u; cube['u'] = 7 - f


N, M, x, y, K = map(int, input().split())                    # 지도 행, 열, 주사위 행, 열, 명령 수
arr = [list(map(int, input().split())) for _ in range(N)]    # 지도

for order in input().split():
    d = int(order) - 1
    nx, ny = x + DIR[d][0], y + DIR[d][1]
    if not (0 <= nx < N and 0 <= ny < M):
        continue
    x, y = nx, ny
    moveCube(d)
    print(cubeNum[cube['u']])
    if arr[x][y] == 0:     # 주사위가 있는 지도의 값이 0이면
        arr[x][y] = cubeNum[7 - cube['u']]
    else:                  # 0이 아니면
        cubeNum[7 - cube['u']] = arr[x][y]
        arr[x][y] = 0
