def solution(n):
    answer = []

    dx = [1, 0, -1]
    dy = [0, 1, -1]

    x, y = 0, 0
    di = 0
    arr = [[0] * n for _ in range(n)]

    for i in range(1, (n * (n + 1)) // 2 + 1):
        arr[x][y] = i

        #       방향이 올바른지
        nx = dx[di] + x
        ny = dy[di] + y

        if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] != 0:
            di += 1
            di %= 3

        #       이동
        x = dx[di] + x
        y = dy[di] + y
    # print(arr)

    for i in range(len(arr)):
        for j in range(i + 1):
            answer.append(arr[i][j])

    return answer