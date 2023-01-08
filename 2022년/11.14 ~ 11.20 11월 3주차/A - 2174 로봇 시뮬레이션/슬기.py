import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

a, b = map(int, input().split())
n, m = map(int, input().split())

command = []
position = dict()
land = [[0] * a for _ in range(b)]
for i in range(1, n+1):
    x, y, pos = input().split()
    if pos == 'N':
        pos = 0
    elif pos == 'E':
        pos = 1
    elif pos == 'S':
        pos = 2
    else:
        pos = 3
    land[b-int(y)][int(x)-1] = 1
    position[i] = [(b-int(y)), int(x)-1, pos]
    # print(position)


for _ in range(m):
    or_robot, order, cnt = input().split()
    command.append([int(or_robot), order, int(cnt)])
    # print(command)

for r, c, repeat in command:
    for _ in range(repeat):
        if c == 'F':
            cur_x, cur_y, di = position[r]
            nx = cur_x + dx[di]
            ny = cur_y + dy[di]
            if not (0 <= nx < b and 0 <= ny < a):
                print("Robot", r, "crashes into the wall")
                exit()
            elif land[nx][ny] == 1:
                for i in position:
                    if nx == position[i][0] and ny == position[i][1]:
                        print("Robot", r, "crashes into robot", i)
                        exit()
            else:
                land[cur_x][cur_y] = 0
                land[nx][ny] = 1
                position[r][0] = nx
                position[r][1] = ny
        elif c == 'L':
            position[r][2] = (position[r][2] - 1) % 4
        else:
            position[r][2] = (position[r][2] + 1) % 4
print('OK')