import sys
sys.stdin = open('input.txt')

# r, s = map(int, input().split())
#
# before = [input() for _ in range(r)]
# after = [['.'] * s for _ in range(r)]
#
# pos = 1 << 14
# print(pos)

def restoreMeteorPicture(picture):
    # 입력된 문자열을 리스트로 변환
    picture = [list(row) for row in picture]

    # 유성의 위치 찾기
    meteor_pieces = []
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            if picture[i][j] == 'X':
                meteor_pieces.append((i, j))

    # 유성 떨어뜨리기
    while True:
        new_meteor_pieces = []
        for i, j in meteor_pieces:
            if i + 1 < len(picture) and picture[i + 1][j] == '.':
                new_meteor_pieces.append((i + 1, j))
                picture[i][j] = '.'
                picture[i + 1][j] = 'X'
        if not new_meteor_pieces:
            break
        meteor_pieces = new_meteor_pieces

    # 결과 출력
    result = [''.join(row) for row in picture]
    return result

# 입력 받기
n, m = map(int, input().split())
picture = []
for _ in range(n):
    row = input()
    picture.append(row)

# 결과 출력
restored_picture = restoreMeteorPicture(picture)
for row in restored_picture:
    print(row)