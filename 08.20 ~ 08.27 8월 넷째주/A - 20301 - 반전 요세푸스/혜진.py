import sys
from collections import deque
sys.stdin = open('input.txt')

n, k, m = map(int, input().split())
Q = deque([i + 1 for i in range(n)])    # 앞, 뒤에서 뽑아 쓸 수 있게 deque 사용

isRight = True                          # 오른쪽방향인가?
cnt = 0                                 # m과 같아지면 방향 전환

while Q:                                # Q를 모두 제거할 때 까지 반복
    if isRight:                         # 오른쪽 방향이면
        for i in range(k - 1):
            Q.append(Q.popleft())       # 앞에서 k - 1명 뒤로 넘기고
        print(Q.popleft())              # 제일 앞 사람 print
    else:                               # 왼쪽 방향이면
        for i in range(k - 1):
            Q.appendleft(Q.pop())       # 뒤에서 k - 1명 앞으로 넘기고
        print(Q.pop())                  # 맨 뒷 사람 print
    cnt += 1

    if cnt == m:                        # m번 반복했으면
        isRight = not isRight           # 방향 바꾸기
        cnt = 0

