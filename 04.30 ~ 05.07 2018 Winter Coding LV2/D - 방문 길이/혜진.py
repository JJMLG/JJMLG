def solution(dirs):
    dic = { 'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0) }
    revDir = { 'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}      # 반대 방향
    r = c = 0               # 시작점
    ans = set()             # 지나간 길 (도착좌표, 어느방향에서 왔는지)
                            # 같은 길을 양방향으로 지날 수 있으니 양방향을 함께 넣어준다
    for d in dirs:
        nr, nc = r + dic[d][0], c + dic[d][1]
        if nr < -5 or nc < -5 or nr > 5 or nc > 5: continue
        
        ans.add((nr, nc, d))
        ans.add((r, c, revDir[d]))
        r, c = nr, nc

    return len(ans) // 2