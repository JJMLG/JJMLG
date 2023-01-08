import sys
sys.stdin = open('input.txt')

student = int(input())

change = list(map(int, input().split()))
want = list(map(int, input().split()))

visited = [0] * 1000001

# 바꾸고 싶은 과목 체크
for i in change:
    visited[i] += 1


cnt = 0
for j in want:
    # 원하는 과목이 있으면 바꾸기 -1 해서 0으로 바꿔 줌
    if visited[j] >= 1:
        visited[j] -= 1
    # 원하는 과목이 없으면 사람 수 추가
    else:
        cnt += 1

print(cnt)