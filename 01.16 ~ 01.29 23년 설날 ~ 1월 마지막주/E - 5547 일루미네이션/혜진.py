"""
바깥에 0으로 된 테두리를 두르고 (0, 0)에서 시작해서 BFS 탐색으로 모든 0들을 탐색한다
그러면 건물 안에있는 0은 제외하고 BFS를 돈다
0의 주변에서 1이 발견되면 ans + 1을 한다
"""
from collections import deque

W, H = map(lambda x:int(x) + 2, input().split())
arr = [[0] * W for _ in range(H)]

for i in range(1, H - 1):
    arr[i][1:W-1] = list(map(int, input().split()))

do = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 0)]        # 홀
de = [(-1, -1), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]      # 짝

Q = deque([(0, 0)])
visited = [[0] * W for _ in range(H)]
visited[0][0] = 1
ans = 0

while Q:
    x, y = Q.popleft()

    d = do if y % 2 else de

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H:
            if arr[ny][nx]:
                ans += 1
            elif not visited[ny][nx]:
                visited[ny][nx] = 1
                Q.append((nx, ny))

print(ans)
