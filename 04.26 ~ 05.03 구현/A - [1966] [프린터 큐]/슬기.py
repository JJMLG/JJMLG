import sys, copy
sys.stdin = open('input.txt')
from collections import deque
from copy import deepcopy


T = int(input())

for _ in range(T):
    # 인풋 받아올 때 마다 q 갱신
    q = deque()
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    # idxlst = list(range(n))
    temp = deepcopy(priority)
    # maxx = max(temp)
    # print(maxx)
    # print(temp, '확인')
    # print(index)

    cnt = 0
    for i in range(n):
        # print(i)

        # 인덱스랑 같이 넣어주기
        q.append((priority[i], i))
        # print(q)
    while q:
        t = q.popleft()
        num = t[0]
        idx = t[1]

        # 맥스값 계속 갱신 (중요도 높은 거 있으면 먼저 빼주기)
        if num == max(temp):
            cnt += 1
            if idx == m:
                print(cnt)
                break
            # 맥스값 바뀌게 해주려고 pop 함
            temp.pop(0)
        else:
            q.append(t)
            temp.append(temp.pop(0))





