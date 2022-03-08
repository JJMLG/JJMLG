import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

ls = list(range(1, n+1))

visited = [0] * (n+1)
arr = [0] * (m+1)

def backtracking(x):
    if visited[x] == 0:
        return 1
    else:
        return 0

def check(y):
    if y == m+1:
        for i in range(1, m+1):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(1, n+1):
            if backtracking(i):     # false 라면?
                visited[i] = 1      # 방문표시
                arr[y] = i          # 숫자 채워주고
                check(y+1)          # 다음 숫자 확인?
                arr[y] = 0          # 초기화
                visited[i] = 0      # 방문 초기화(숫자 초기화)

check(1)