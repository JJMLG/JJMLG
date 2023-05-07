def solution(dirs):
    answer = set()  # set()을 통해 중복을 제거
    d = {"U": [1, 0], "D": [-1, 0], "R": [0, 1], "L": [0, -1]}

    x, y = 0, 0

    # 반복문을 통해 명령어를 수행
    for i in dirs:
        dx, dy = d[i]

        # 이동해야하는 좌표
        nx = x + dx
        ny = y + dy

        # 범위 내에 있다면 명령어 수행
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((x, y, nx, ny))  # 현재 위치 -> 이동 후 위치
            answer.add((nx, ny, x, y))  # 이동 후 위치 -> 현재 위치
            x, y = nx, ny  # 이동 위치로 현재 위치 변경

    # answer를 2로 나눴을 때 몫이 처음 걸어본 길이가 된다.
    return len(answer) // 2