from collections import deque


def solution(park, routes):
    answer = []

    w = len(park)
    h = len(park[0])

    s = 0
    e = 0
    for i in range(w):
        for j in range(h):
            if park[i][j] == 'S':
                s = j
                e = i
                break

    for i in routes:
        # 위치 초기화
        x = s
        y = e

        for j in range(int(i[2])):
            # 동쪽 : 현재 위치가 map 가장 오른쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            if i[0] == 'E' and x != h - 1 and park[y][x + 1] != 'X':
                x += 1
                if j == int(i[2]) - 1:
                    s = x  # step만큼 움직였으면 위치 초기화
            # 서쪽 : 현재 위치가 map 가장 왼쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif i[0] == 'W' and x != 0 and park[y][x - 1] != 'X':
                x -= 1
                if j == int(i[2]) - 1:
                    s = x
            # 남쪽 : 현재 위치가 map 가장 아래쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif i[0] == 'S' and y != len(park) - 1 and park[y + 1][x] != 'X':
                y += 1
                if j == int(i[2]) - 1:
                    e = y
            # 북쪽 : 현재 위치가 map 가장 위쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif i[0] == 'N' and y != 0 and park[y - 1][x] != 'X':
                y -= 1
                if j == int(i[2]) - 1:
                    e = y

    return [y, x]


# from collections import deque
#
#
# def solution(park, routes):
#     answer = []
#
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#
#     def bfs(x, y):
#         q = deque()
#         q.append([x, y])
#
#         while q:
#             t = q.popleft()
#             # print(t)
#             nx = t[0]
#             ny = t[1]
#             for m in routes:
#                 if m[0] == 'N':
#                     nx -= int(m[2])
#                 elif m[0] == 'S':
#                     nx += int(m[2])
#                 elif m[0] == 'W':
#                     ny -= int(m[2])
#                 else:
#                     ny += int(m[2])
#
#             nxx = nx
#             nyy = ny
#             for k in range(4):
#                 nxx = dx[k] + nx
#                 nyy = dy[k] + ny
#
#                 if 0 <= nxx < w and 0 <= nyy < h:
#                     print(nxx, nyy, '??')
#                     if visited[nxx][nyy] == 1:
#                         print(nxx, nyy, visited)
#                 #     print(nxx, nyy, visited)
#                 #     if visited[nxx][nyy] == 0:
#                 #         visited[nxx][nyy] = 1
#                 #         q.append([nxx, nyy])
#                 #         print(nxx, nyy)
#                 #     else:
#                 #         print(nxx, nyy, '???')
#                 #         continue
#
#     w = len(park)
#     h = len(park[0])
#
#     visited = [[0] * h for _ in range(w)]
#     # print(visited)
#
#     s = 0
#     e = 0
#     for i in range(w):
#         for j in range(h):
#             if park[i][j] == 'S':
#                 visited[i][j] = 2
#                 s = i
#                 e = j
#             elif park[i][j] == 'X':
#                 visited[i][j] = 1
#
#     a = bfs(s, e)
#     # print(a)
#     # print(visited)
#
#     return answer