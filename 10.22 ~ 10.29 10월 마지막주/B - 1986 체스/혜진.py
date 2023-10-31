N, M = map(int, input().split())
queen = list(map(int, input().split()))
qn = queen.pop(0)
knight = list(map(int, input().split()))
kn = knight.pop(0)
pawn = list(map(int, input().split()))
pn = pawn.pop(0)
qdir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
kdir = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

arr = [[''] * M for _ in range(N)]
check = [[1] * M for _ in range(N)]
for n in range(qn):
    queen[n*2] -= 1
    queen[n*2+1] -= 1
    arr[queen[n*2]][queen[n*2+1]] = 'q'
for n in range(kn):
    knight[n*2] -= 1
    knight[n*2+1] -= 1
    arr[knight[n*2]][knight[n*2+1]] = 'k'
for n in range(pn):
    pawn[n*2] -= 1
    pawn[n*2+1] -= 1
    arr[pawn[n*2]][pawn[n*2+1]] = 'p'

for n in range(kn):
    r, c = knight[n*2], knight[n*2+1]
    for d in range(8):
        nr, nc = r + kdir[d][0], c + kdir[d][1]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '':
            check[nr][nc] = 0

for n in range(qn):
    for d in range(8):
        r, c = queen[n*2], queen[n*2+1]
        dr, dc = qdir[d][0],  qdir[d][1]
        while True:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '':
                check[nr][nc] = 0
                r, c = nr, nc
            else:
                break

ans = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == '' and check[r][c]:
            ans += 1
print(ans)
