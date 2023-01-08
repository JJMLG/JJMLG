def in_map(i, j):
    return 0 <= i < N and 0 <= j < M


def spread():       # 불 번짐
    next = []
    for i, j in fire:
        for di, dj in d:
            ni, nj = i + di, j + dj
            if in_map(ni, nj) and arr[ni][nj] == ".":
                arr[ni][nj] = "*"
                next.append((ni, nj))

    return next


def go_out():       # 탈출시도, 방문한 곳은 다시 가지 않음
    next = []
    for i, j, t in sg:
        for di, dj in d:
            ni, nj = i + di, j + dj
            if in_map(ni, nj):
                if arr[ni][nj] == "." and not vis[ni][nj]:
                    vis[ni][nj] = 1
                    next.append((ni, nj, t + 1))

            else:   # 탈출 성공
                return t + 1

    return next


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(int(input())):
    M, N = map(int, input().split())
    arr, fire, sg = [], [], []          # 배열 (#: 벽), (*: 불), (.: 빈공간)
    vis = [[0] * M for _ in range(N)]   # 되돌아가지 않도록 방문 확인
    ans = "IMPOSSIBLE"                  # string 아니고 int면 반복문 탈출
    
    for i in range(N):
        lst = list(input())
        for j in range(M):
            if lst[j] == "*":           # 불이야
                fire.append((i, j))
            elif lst[j] == "@":         # 사람있어요
                lst[j] = "."            # 사람자리엔 불이 번질 수 있다
                sg.append((i, j, 0))    # 상근
                vis[i][j] = 1           # 첫 자리도 방문처리
        arr.append(lst)

    while sg:
        fire = spread()
        sg = go_out()

        if type(sg) == int:
            ans = sg
            break

    print(ans)
