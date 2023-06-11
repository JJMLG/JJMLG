def solution(park, routes):
    sr = sc = -1                    # 시작 좌표 찾기
    for i in range(len(park)):
        if sr == -1:
            tmp = park[i].find('S') # find => 없으면 -1, 있으면 해당 index
            if tmp > -1:
                sr, sc = i, tmp
                break               # 시작 좌표 찾았으면 그만

    
    def cango(route, r, c):
        dic = { 'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1) }
        d = dic[route[0]]
        n = int(route[2])
        R, C = r, c

        for i in range(n):
            nr, nc = r + d[0], c + d[1]
            if 0 > nr or 0 > nc or len(park) <= nr or len(park[0]) <= nc:
                return (False, )
            if park[nr][nc] == 'X':
                return (False, )
            r, c = nr, nc
        return True, r, c

    for route in routes:
        flag = cango(route, sr, sc)
        if flag[0]:
            sr, sc = flag[1], flag[2]
    
    return [sr, sc]



print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))       # [2,1]
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))       # [0,1]
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])) # [0,0]
