from collections import deque


def solution(maps):
    answer = []

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(x, y):
        cnt = 0
        q = deque()
        q.append([x, y])
        visited[x][y] = 1

        while q:
            t = q.popleft()
            cnt += int(maps[t[0]][t[1]])

            for k in range(4):
                nx = dx[k] + t[0]
                ny = dy[k] + t[1]

                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                    visited[nx][ny] = 1
                    # cnt += int(maps[nx][ny])
                    q.append([nx, ny])

        # print(cnt)
        return cnt

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                answer.append(bfs(i, j))
                # answer.append(cnt)
    answer.sort()

    if not answer:
        answer.append(-1)

    return answer