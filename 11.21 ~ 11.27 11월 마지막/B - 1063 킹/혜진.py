d = {
        'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0),
        'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)
    }
arr = [[0] * 8 for _ in range(8)]

king, stone, n = input().split()
move = [d[input()] for _ in range(int(n))]

A = ord('A')
kc, kr = ord(king[0]) - A, int(king[1]) - 1
sc, sr = ord(stone[0]) - A, int(stone[1]) - 1
arr[kr][kc] = 'k'
arr[sr][sc] = 's'

def in_map(r, c):
    return 0 <= r < 8 and 0 <= c < 8

for dr,dc in move:
    nr, nc = kr + dr, kc + dc
    if in_map(nr, nc):
        if arr[nr][nc] == "s":      # 돌이 있으면
            ni, nj = sr + dr, sc + dc
            if in_map(ni, nj):      # 돌이 map 안에 있으면 돌 움직이고 왕도 움직인다
                arr[ni][nj] = 's'   # 돌 전진 (돌 자리는 왕이 덮어쓰니까 비우기 안함)
                sr, sc = ni, nj
            else:                   # 돌이 벗어나면 king도 넘어감
                continue
        arr[kr][kc] = 0             # 왕 자리 비우고
        arr[nr][nc] = 'k'           # 와 전진
        kr, kc = nr, nc

print(chr(kc + A) + str(kr + 1))
print(chr(sc + A) + str(sr + 1))
