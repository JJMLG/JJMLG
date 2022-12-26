import sys
from collections import deque
sys.stdin = open('4991.txt')

DIR=[(-1,0), (0,1), (1,0), (0,-1)]
def DFS(dep):
    if(dep == len(dirties)):
        # print(permut, "==============")
        nr = dirties[permut[0]][0]
        nc = dirties[permut[0]][1]
        totalD = memo[SR][SC][nr][nc]
        for idx in range(len(dirties)-1):
            sr = dirties[permut[idx]][0]
            sc = dirties[permut[idx]][1]
            er = dirties[permut[idx+1]][0]
            ec = dirties[permut[idx+1]][1]
            ret = memo[sr][sc][er][ec]
            # print(sr,sc,er,ec, ret)
            totalD += ret
        global maxx
        if maxx > totalD:
            maxx = totalD
        return
    for rep in range(len(dirties)):
        if permvisit[rep]:
            continue
        permvisit[rep] = 1
        permut.append(rep)
        DFS(dep+1)
        permvisit[rep] = 0
        permut.pop()
def BFS(sr, sc, er, ec):
    visit = [[0 for _ in range(W+1)] for _ in range(H+1)]
    dq = deque()
    dq.append([sr, sc, 0])
    visit[sr][sc] = 1
    while dq:
        nr, nc, dis = dq.popleft()
        for idx in range(4):
            dy = nr + DIR[idx][0]
            dx = nc + DIR[idx][1]
            newdis = dis+1
            if(dy<0 or dx<0 or dy>=H or dx>=W):
                continue
            if(maps[dy][dx]=='x'):
                continue
            if visit[dy][dx]:
                continue
            if(dy == er and dx == ec):
                return newdis
            visit[dy][dx] = 1
            dq.append([dy, dx, newdis])
    return -1
def makePath():
    for c in range(len(dirties)):
        ret = BFS(SR, SC, dirties[c][0], dirties[c][1])
        if ret == -1:
            return 0
        memo[SR][SC][dirties[c][0]][dirties[c][1]] = ret
        memo[dirties[c][0]][dirties[c][1]][SR][SC] = ret
    for r in range(len(dirties)-1):
        for c in range(r+1, len(dirties)):
            sr, sc = dirties[r]
            er, ec = dirties[c]
            ret = BFS(sr, sc, er, ec)
            if ret==-1:
                return 0
            memo[sr][sc][er][ec] = ret
            memo[er][ec][sr][sc] = ret
    return 1
    # bfs()

while(1):
    W,H  = map(int, input().split())
    if not W and not H:
        break
    else:
        # 맵정보
        maps = []
        # 더러운 방정보
        dirties = []
        SR = SC = 0
        # 데이터 입력
        for r in range(H):
            word = input()
            maps.append(word)
            for c in range(len(word)):
                if word[c] == '*':
                    dirties.append([r,c])
                elif word[c] == 'o':
                    SR = r
                    SC = c
        maxx = 0x7fffffff
        permut = []
        permvisit = [0 for _ in range(len(dirties)+1)]
        # 출발지점과 도착지점 거리 입력
        memo = [[[[0 for _ in range(W+1)] for _ in range(H+1)] for _ in range(W+1)] for _ in range(H+1)]
        ret = makePath()
        # 만약에 못가는 길이 있으면 끝내기
        if not ret:
            print(-1)
            continue
        else:
            DFS(0)
            print(maxx)