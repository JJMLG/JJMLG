def crushpop(m, n, arr):
    crush = set()   # 터뜨릴 좌표 모음
    for r in range(m - 1):
        for c in range(n - 1):
            if arr[r][c] == '': continue
            if arr[r][c] == arr[r][c+1] == arr[r+1][c] == arr[r+1][c+1]:
                crush.add((r, c)); crush.add((r, c+1))
                crush.add((r+1, c)); crush.add((r+1, c+1))
    if len(crush) == 0: return 0    # 터질게 없으면 0
    for i, j in list(crush):        # 터뜨리기
        arr[i][j] = ''
    for r in range(m - 2, -1, -1):  # 밑에서부터 차근차근 내려주기
        for c in range(n):
            y = r                   # r행에서 y행으로 내려간다
            while y + 1 < m and arr[y + 1][c] == '':
                y += 1              # 아래칸이 board안에 있고 비었으면 내려간다
            if y == r: continue     # 내려갈거 없으면 pass
            arr[y][c] = arr[r][c]   # 내려준다
            arr[r][c] = ''
    return len(crush)

def solution(m, n, board):  # m:행, n:열
    for i in range(m):
        board[i] = list(board[i])
    ans = 0
    while True:
        cp = crushpop(m, n, board)
        if not cp: break
        ans += cp
    return ans
