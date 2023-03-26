from collections import deque


def check(arr):
    visited = [[1]*5 for _ in range(5)]

    for a in arr:
        y, x = a
        visited[y][x] = 0
    
    Q = deque([(arr[0])])
    y, x = arr[0]
    visited[y][x] = 1
    cnt = 1

    while Q:
        y, x = Q.popleft()

        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]

            if 0<=ny<5 and 0<=nx<5 and not visited[ny][nx]:
                visited[ny][nx] = 1
                cnt += 1
                Q.append((ny, nx))

    return True if cnt == 7 else False


def DFS(depth, idx, YDY_cnt):
    global result

    if YDY_cnt>=4:
        return
    
    if depth == 7:
        if check(arr):
            result += 1
        return
    
    for i in range(idx, 25):
        y, x = i//5, i%5
        arr.append((y, x))
        DFS(depth+1, i+1, YDY_cnt+(students[y][x]=='Y'))
        arr.pop()


dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

students = [input() for _ in range(5)]
result = 0
arr = []

DFS(0, 0, 0)

print(result)

"""
DFS를 통해 조합 짜듯이, 7명의 학생을 행 열 상관없이 선택한다
    임도연파가 4명이상이면 무효이므로 return 한다
7명을 선택했다면 상하좌우로 붙어있는지 확인한다
방문배열을, 선택된 학생들 자리만 0으로 설정하고 한 명 씩 확인하면서 cnt++ 한다
7명의 학생이 상하좌우로 붙어있다면 result++ 한다

7명의 학생을 선택하는 과정에서 시간을 줄이는 것이 중요했던 문제
"""