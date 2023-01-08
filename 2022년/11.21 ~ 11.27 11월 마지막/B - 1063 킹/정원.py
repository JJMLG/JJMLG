import sys

input = sys.stdin.readline

A_to_num = {
    'A':0, 'B':1, 'C':2, 'D':3,
    'E':4, 'F':5, 'G':6, 'H':7,
}
num_to_A = {
    0:'A', 1:'B', 2:'C', 3:'D',
    4:'E', 5:'F', 6:'G', 7:'H',
}
# R L B T RT LT RB LB
dy = [0, 0, 1, -1, -1, -1, 1, 1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
order_to_idx = {
    'R':0, 'L':1, 'B':2, 'T':3,
    'RT':4, 'LT':5, 'RB':6, 'LB':7,
}

def piece_to_arr(coordinate, value):
    i, j = 0, 0
    for c in coordinate:
        try:
            i = 8-(int(c))
        except:
            j = A_to_num[c]
    arr[i][j] = value

king, stone, N = input().rstrip().split()
arr = [[0]*8 for _ in range(8)]

# 킹, 돌 좌표 배열에 저장
piece_to_arr(king, 1)
piece_to_arr(stone, 2)

# 명령 입력받고 이동
for n in range(int(N)):
    order = input().rstrip()
    print(order)
    k = order_to_idx[order]
    ky, kx = 0, 0
    sy, sx = 0, 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 1:
                ky, kx = i, j
            if arr[i][j] == 2:
                sy, sx = i, j
    nky, nkx = ky+dy[k], kx+dx[k] # new king
    if 0<=ky<8 and 0<=kx<8:
        if nky != sy and nkx != sx:
            arr[ky][kx], arr[nky][nkx] = 0, 1
        else: # 킹이 돌을 밀 때
            nsy, nsx = sy+dy[k], sx+dx[k]
            if 0<=nsy<8 and 0<=nsx<8:
                arr[ky][kx], arr[nky][nkx], arr[nsy][nsx] = 0, 1, 2

#　결과값 출력
result = [[], []]
for i in range(8):
    for j in range(8):
        if arr[i][j] == 1:
            result[0].append(j)
            result[0].append(i)
        if arr[i][j] == 2:
            result[1].append(j)
            result[1].append(i)
for r in result:
    print(num_to_A[r[0]], end='')
    print(8-r[1])

"""
킹의 8방향 델타이동
    킹이 체스판 밖으로 나가지 않는 경우
        킹이 돌을 밀지 않을 때
        킹이 돌을 밀 때
            돌이 체스판 밖으로 나가지 않는 경우
            돌이 체스판 밖으로 나가는 경우
    킹이 체스판 밖으로 나가는 경우
"""