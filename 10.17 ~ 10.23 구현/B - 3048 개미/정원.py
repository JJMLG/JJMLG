N, M = map(int, input().split())
ants1, ants2 = list(input()), list(input())
T = int(input())
arr = []
for i in range(N): arr.append((ants1[::-1][i], 1)) # 오른쪽으로 가려고 함, 배열이 뒤집히는 점에 주의
for i in range(M): arr.append((ants2[i], -1)) # 왼쪽으로 가려고 함
time = 0
while time < T: # T초동안 움직일 것
    time += 1
    i = 0
    while i < N+M-1:
        ant1, ant2 = arr[i], arr[i+1]
        if ant1[1] == 1 and ant2[1] == -1: # 진행하려는 방향이 교차하는 경우
            arr[i], arr[i+1] = arr[i+1], arr[i] # 서로 자리를 바꿔준다 == 두 개미중 하나가 점프
            i += 1 # 인덱스 추가로 하나 더 늘려주기
        i += 1 # 다음 개미 탐색
for a in arr: print(a[0], end='')