import sys
sys.stdin = open('input.txt')


def check(arr):
    n = len(arr)
    answer = 1

    for x in range(n):
        # 열 순회하면서 연속되는 숫자 찾기
        cnt = 1
        for y in range(1, n):
            if arr[x][y] == arr[x][y-1]:
                # 이전 사탕과 같다면 cnt + 1
                cnt += 1
            else:
                # 다르면 다시 1로 초기화
                cnt = 1

            # 비교해서 현재 cnt가 더 크면 candy 갱신
            if cnt > answer:
                answer = cnt

        # 행 순회하면서 연속되는 숫자 찾기
        cnt = 1
        for y in range(1, n):
            if arr[y][x] == arr[y-1][x]:
                cnt +=1
            else:
                cnt = 1

            if cnt > answer:
                answer = cnt

    return answer

board = int(input())

arr = [list(input()) for _ in range(board)]
# print(arr)
candy = 0

for i in range(board):
    for j in range(board):
        # 열 바꾸기
        if j + 1 < board:
            # 인접한 사탕 바꾸기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            # 인접한 사탕 바꿨을 때 가장 긴 연속한 부분 찾아 내는 함수 돌리기
            tmp = check(arr)

            if tmp > candy:
                candy = tmp

            # 다시 원상태로 돌리기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        # 행 바꾸기
        if i + 1 < board:
            # 인접한 사탕 바꾸기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            # 사탕 바꿨을 때 긴 연속 부분 찾기
            tmp = check(arr)

            if tmp > candy:
                candy = tmp

            # 다시 원상태로 돌려주기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(candy)