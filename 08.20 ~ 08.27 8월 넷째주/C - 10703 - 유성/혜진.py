import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
pic = [input() for _ in range(N)]

moveRow = N                                     # 아래로 몇칸 이동할지
for c in range(M):
    lastStarRow = lastLandRow = -1              # 같은 열에서 마지막 유성 index, 첫 땅 index
    for r in range(N):
        if pic[r][c] == 'X':
            lastStarRow = r
        if lastLandRow == -1 and pic[r][c] == '#':
            lastLandRow = r
    if lastLandRow >= 0 and lastStarRow >= 0:   # 이동할 칸 수 업데이트
        moveRow = min(moveRow, lastLandRow - lastStarRow - 1)

ans = [list(pic[i]) for i in range(N)]
for c in range(M):
    for  r in range(N - 1, -1 , -1):
        if ans[r][c] == 'X':                    # 가장 아래에 있는 유성부터 이동
            ans[r + moveRow][c] = 'X'
            ans[r][c] = '.'
for r in range(N):
    print(''.join(ans[r]))
