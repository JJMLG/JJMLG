def solution(wallpaper):
    answer = []
    pos = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                pos.append([i,j])
    
    maxX = pos[0][0]
    minX = pos[0][0]
    maxY = pos[0][1]
    minY = pos[0][1]
    for i in pos:
        if i[0] > maxX:
            maxX = i[0]
        if i[0] < minX:
            minX = i[0]
        if i[1] > maxY:
            maxY = i[1]
        if i[1] < minY:
            minY = i[1]
    
    answer = (minX,minY,maxX+1,maxY+1)
    return answer