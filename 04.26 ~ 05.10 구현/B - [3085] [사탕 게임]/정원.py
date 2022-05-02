import sys

N = int(sys.stdin.readline())
arr = [list(map(str, input())) for _ in range(N)]
result = 0 # 결과 최대값

def check(arr): # 현재 배열에서 최대값을 확인함
    cnt = 0 # 배열에서 확인할 최대값 초기화
    for i in range(N):
        row = 1 # 행, 가로
        col = 1 # 열, 세로
        # 최대길이를 파악하는 방향은 한 쪽 방향이다
        # 하지만 배열의 모든 좌표에 대해서 진행하므로 문제없음!
        for j in range(N-1): 
            if arr[i][j] == arr[i][j+1]: # 연속할 경우
                row += 1 # 길이++
            else: # 연속하지 않을 경우 다시 1부터
                cnt = max(cnt, row) # 갱신 한 번 해주고
                row = 1
                
            if arr[j][i] == arr[j+1][i]: # 연속할 경우
                col += 1 # 길이++
            else: # 연속하지 않을 경우 다시 1부터
                cnt = max(cnt, col) # 갱신 한 번 해주고
                col = 1
        cnt = max(cnt, row, col) # 기존cnt, 행, 열의 각각 값들 중 최대값 갱신
    return cnt

for i in range(N):
    for j in range(N-1):
        # 위치를 바꿔서 같으면 옮길 필요가 없음
        # 가로 옮겨보고
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            result = max(result, check(arr)) # 최대값 갱신
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        # 세로 옮겨보고
        if arr[j][i] != arr[j+1][i]:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            result = max(result, check(arr)) # 최대값 갱신
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            
print(result) # 최대값 출력