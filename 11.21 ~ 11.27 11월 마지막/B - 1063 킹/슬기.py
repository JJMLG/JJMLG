import sys
sys.stdin = open('input.txt')

king, rock, n = input().split()
n = int(n)
k_row, k_col = king[0], int(king[1])
r_row, r_col = rock[0], int(rock[1])

alpha = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
k_row = alpha[k_row]
r_row = alpha[r_row]

move = {
    'R': [1, 0],
    'L': [-1, 0],
    'B': [0, -1],
    'T': [0, 1],
    'RT': [1, 1],
    'LT': [-1, 1],
    'RB': [1, -1],
    'LB': [-1, -1],
}

for _ in range(n):
    order = input()
    nx = k_row + move[order][0]
    ny = k_col + move[order][1]

    if 0 < nx <= 8 and 0 < ny <= 8:
        if nx == r_row and ny == r_col:
            dx = r_row + move[order][0]
            dy = r_col + move[order][1]

            if 0 < dx <= 8 and 0 < dy <= 8:
                k_row = nx
                k_col = ny
                r_row = dx
                r_col = dy
        else:
            k_row = nx
            k_col = ny

k_res = ''
r_res = ''
for k, v in alpha.items():
    if v == k_row:
        k_res += k
        k_res += str(k_col)
    if v == r_row:
        r_res += k
        r_res += str(r_col)
print(k_res)
print(r_res)
