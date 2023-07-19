def solution(board):
    R, C = len(board), len(board[0])
    ans = 0
    for r in range(1, R):          # 한 변이 2인 사각형부터 확인하려고 1부터 시작
        for c in range(1, C):
            if board[r][c]:        # 0이면 어차피 사각형 안됨
                x = board[r - 1][c]
                y = board[r][c - 1]
                z = board[r - 1][c - 1]
                board[r][c] = min(x, y, z) + 1
                ans = max(board[r][c], ans)
    return ans * ans        # 한 변 길이 구했으니까 넓이 return
