import sys

column = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
}
rColumn = {v:k for k,v in column.items()}
move = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[-1,-1],[1,1],[1,-1]]
d = {
    'R': 0,
    'L': 1,
    'B': 2,
    'T': 3,
    'RT': 4,
    'LT': 5,
    'RB': 6,
    'LB': 7,
}

king, stone, n = input().split()
n = int(n)

arr = [[0]*8 for _ in range(8)]

arr[8-int(king[1])][column[king[0]]] = 1
arr[8-int(stone[1])][column[stone[0]]] = 2

x = 8-int(king[1])
y = column[king[0]]

for i in range(n):
    go = input()
    nx = x + move[d[go]][0]
    ny = y + move[d[go]][1]

    if nx < 0 or nx >= 8 or ny < 0 or ny >=8:
        continue
    
    if arr[nx][ny] == 2:
        sx = nx+move[d[go]][0]
        sy = ny+move[d[go]][1]
        if sx < 0 or sx >= 8 or sy < 0 or sy >=8:
            continue

        arr[nx][ny] = 1
        arr[sx][sy] = 2
    arr[x][y] = 0
    x = nx
    y = ny
    arr[x][y] =1

ans1 = ''
ans2 = ''
for i in range(8):
    for j in range(8):
        if arr[i][j] == 1:
            ans1 = rColumn[j] + str(8-i)
        if arr[i][j] == 2:
            ans2 = rColumn[j] + str(8-i) 

print(ans1)
print(ans2)