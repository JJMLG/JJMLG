import sys
sys.stdin = open('input.txt')
from collections import deque




def bfs(s):
    # +1, -1, +a, -a, +b, -b, *a, *b칸 이동
    dx = [-1, 1, -a, a, -b, b, a, b]
    q = deque([s])
    # q.append(s)
    visited[s] = 1

    while q:
        now = q.popleft()

        for i in range(8):
            # 6가지는 +, - 연산
            if i < 6:
                nx = now + dx[i]

                if 0 <= nx <= 100000 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    bridge[nx] = bridge[now] + 1

            # 2가지는 곱하기 연산
            else:
                ny = now * dx[i]

                if 0 <= ny <= 100000 and visited[ny] == 0:
                    q.append(ny)
                    visited[ny] = 1
                    bridge[ny] = bridge[now] + 1


a, b, n, m = list(map(int, input().split()))

bridge = [0 for _ in range(100001)]
visited = [0 for _ in range(100001)]

bfs(n)
print(bridge[m])


"""
1. +1
2. -1
3. +a
4. -a
5. +b
6. -b
7. *a
8. *b
"""