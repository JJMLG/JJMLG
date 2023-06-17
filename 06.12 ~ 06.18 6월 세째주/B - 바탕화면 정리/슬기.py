from pprint import pprint


def solution(wallpaper):

    x = int(1e9)
    xx = 0
    y = int(1e9)
    yy = 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                # print(i, j)
                if x >= i:
                    x = i
                if xx <= i:
                    xx = i
                if y >= j:
                    y = j
                if yy <= j:
                    yy = j

    return [x, y, xx + 1, yy + 1]