def find(height, width):
    global result
    for i in range(height-1):
        j = 0
        while j < width-1:
            j += 1
            if arr[i][j:j+2] == 'XX' and arr[i+1][j:j+2] == '..':
                result += 1
                j += 1
            if arr[i][j:j+2] == '..' and arr[i+1][j:j+2] == 'XX':
                result += 1
                j += 1

def rotate(arr):
    new_arr = []
    for j in range(M):
        tmp = ''
        for i in range(N):
            tmp += arr[i][j]
        new_arr.append(tmp)
    return new_arr

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
result = 0
find(N, M)
arr = rotate(arr)
find(M, N)
print(result)

"""
그림을 걸 수 있는지 가로로만 스캔할 것
그리고 배열을 90도 돌려주고 다시 스캔
주의할 점은
90도만 배열을 돌리기 때문에 N과 M이 반전됨
"""