directions = ['d', 'l', 'r', 'u']
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

ok = False
answer = ''


def solution(n, m, x, y, r, c, k):
    global answer

    def dfs(px, py, cnt, way):
        global ok, answer
        # 최단경로 발견했다면 스탑
        if ok:
            return
        # 현재 거리가 목표지점에서 멀어지면 스탑
        if abs(px - r) + abs(py - c) + cnt > k:
            return

        # k보다 더 많이 이동했다면 스탑
        if cnt > k:
            return

        if not ok and cnt == k:
            if px == r and py == c:
                ok = True
                answer = way
            return

        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]

            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue

            dfs(nx, ny, cnt + 1, way + directions[d])

    z = k - abs(x - r) + abs(y - c)
    if z < 0 or z % 2 != 0:
        return 'impossible'

    dfs(x, y, 0, '')
    if not ok:
        return "impossible"

    return answer