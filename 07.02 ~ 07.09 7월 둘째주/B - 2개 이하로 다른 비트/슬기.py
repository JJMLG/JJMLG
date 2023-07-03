from collections import deque


def solution(x, y, n):
    answer = 0
    cnt = 0

    flag = 0

    def bfs(y, cnt):
        nonlocal flag
        q = deque()
        q.append([y, cnt])

        while q:
            t = q.popleft()
            # print(t)
            if t[0] == x:
                flag = 1
                return t[1]

            if t[0] > x:
                if t[0] % 3 == 0:
                    q.append([t[0] // 3, t[1] + 1])

                if t[0] % 2 == 0:
                    q.append([t[0] // 2, t[1] + 1])
                q.append([t[0] - n, t[1] + 1])

        if not flag:
            return -1

    answer = bfs(y, cnt)

    return answer