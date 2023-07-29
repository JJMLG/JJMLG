def solution(board):
    answer = 1 if 1 in board[0] or 1 in board[-1] else 0
    for m in range(1,len(board)):
        for n in range(1,len(board[0])):
            if board[m][n] == 1:
                board[m][n] = min(board[m-1][n], board[m-1][n-1], board[m][n-1]) + 1
                if board[m][n] > answer:
                    answer = board[m][n]

    return answer ** 2

"""
2중 포문을 이용해서 원소 하나하나에 방문한다.
현재의 위치에서 가능한 최대 크기의 정사각형의 한 변의 길이를 dp에 저장한다.
아래와 같은 과정을 하나씩 해보면 알겠지만 '현재의 위치에서 가능한 최대 크기의 정사각형의
한 변의 길이'는 현재 위치가 [i][j]라면 dp[i-1][j-1], dp[i-1][j], dp[i][j-1] 이렇게 세 값을 비교했을 때 가장 작은 값에 1을 더한 값이다!
(단, 현재 위치의 board값이 1일 때!)
"""

def solution(board):
    n = len(board)
    m = len(board[0])

    # 2중 포문으로 연산
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], dp[i][j - 1]) + 1

    # 최대 넓이 구하기
    answer = 0
    for i in range(n):
        temp = max(board[i])
        answer = max(answer, temp)

    return answer ** 2