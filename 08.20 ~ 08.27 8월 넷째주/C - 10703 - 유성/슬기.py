import sys
sys.stdin = open('input.txt')

r, s = map(int, input().split())

before = [input() for _ in range(r)]
after = [['.'] * s for _ in range(r)]

pos = 1 << 14   # 유성이 최종적으로 움직여야하는 거리
# print(pos)

for i in range(s):
    h_meteor = 0    # 가장 높은 유성 행 좌표 (좌표가 높아야 땅과의 거리가 가깝다.)
    h_ground = 9999     # 가장 낮은 땅 행 좌표 (좌표가 낮아야 유성과의 거리가 가깝다.)
    flag = 0
    for j in range(r):
        if before[j][i] == 'X':
            # print(before)
            h_meteor = max(h_meteor, j)
            flag = 1    # 유성이 있는 좌표를 만나면
        elif before[j][i] == '#':
            h_ground = min(h_ground, j)
    if flag:    # 유성이 있는 좌표에서 pos 계산
        pos = min(abs(h_meteor-h_ground)-1, pos)
        # print(pos)

for i in range(r):
    for j in range(s):
        if before[i][j] == 'X':
            after[i+pos][j] = 'X'   # 유성을 최종 pos만큼 움직임
        if before[i][j] == '#':
            after[i][j] = '#'

for i in range(r):
    print(''.join(after[i]))