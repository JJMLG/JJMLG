def solution(wallpaper):
    a = b = 50      # 왼쪽 위
    c = d = 0       # 오른쪽 아래
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '.': continue
            if i < a:
                a = i
            if j < b:
                b = j
            if i > c:
                c = i
            if j > d:
                d = j
    return [a, b, c + 1, d + 1]
