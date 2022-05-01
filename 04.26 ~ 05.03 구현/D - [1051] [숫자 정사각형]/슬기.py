import sys, copy
sys.stdin = open('input.txt')

n, m = map(int, input().split())
# print(n, m)
arr = [list(map(int, input())) for _ in range(n)]
# print(arr)

# 모르겠음
check = min(n, m)
answer = 0
for i in range(n):
    for j in range(m):
        for k in range(check):
            # 벽 체크와 상하좌우 비교 하는 부분
            if ((i + k) < n) and ((j + k) < m) and (arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]):
                answer = max(answer, (k + 1) ** 2)

print(answer)