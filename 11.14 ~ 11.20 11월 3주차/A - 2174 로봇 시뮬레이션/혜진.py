A, B = map(int, input().split())            # 가로 A, 세로 B
N, M = map(int, input().split())            # 로봇 N개, 명령 M개

now = {}                                    # { 로봇번호: [r, c, NESW] }
arr = [[0] * A for _ in range(B)]           # 위치에 존재하는 로봇 번호
ans = "OK"                                  # 첫번째 충돌만 출력이니까 OK가 아니면 반복문 탈출

for n in range(1, N + 1):
    x, y, d = input().split()
    r = B - int(y)
    c = int(x) - 1
    now[n] = [r, c, d]
    arr[r][c] = n

d = "NESW"
nd = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

for _ in range(M):
    robot, order, cnt = input().split()     # 로봇번호, 명령, 반복
    robot, cnt = int(robot), int(cnt)
    NESW = now[robot][2]                    # 이 번호의 로봇이 보는 방향

    if order == "F":            # 전진
        r, c = now[robot][0], now[robot][1]
        while cnt > 0 and ans == "OK":
            nr, nc = r + nd[NESW][0], c + nd[NESW][1]
            if 0 <= nr < B and 0 <= nc < A:
                if arr[nr][nc]:
                    ans = "Robot {} crashes into robot {}".format(robot, arr[nr][nc])
                else:
                    arr[r][c] = 0
                    arr[nr][nc] = robot
                    r, c = nr, nc
                    now[robot] = [r, c, now[robot][2]]
            else:
                ans = "Robot {} crashes into the wall".format(robot)
            cnt -= 1

    else:                       # 회전
        cnt %= 4
        idx = d.index(NESW)     # 0123 숫자로 바꿔야 cnt로 계산하기 쉽다
        idx = idx + cnt if order == "R" else idx + 4 - cnt
        idx %= 4                # NESW에서 찾아야하니까
        now[robot][2] = d[idx]

    if ans != "OK": break       # 충돌이 발생했으면 반복문 탈출

print(ans)
