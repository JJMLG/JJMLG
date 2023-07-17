def solution(board):
    R, C = len(board), len(board[0])
    ans = 0
    for r in range(1, R):
        for c in range(1, C):
            if board[r][c]:
                x = board[r - 1][c]
                y = board[r][c - 1]
                z = board[r - 1][c - 1]
                board[r][c] = min(x, y, z) + 1
                ans = max(board[r][c], ans)
    return ans * ans
