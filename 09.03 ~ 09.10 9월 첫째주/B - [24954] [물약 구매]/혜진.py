import sys
from itertools import permutations  # 순열
sys.stdin = open('input.txt')

N = int(input())
origin = list(map(int, input().split()))
sale = [[] for _ in range(N)]       # i를 사면 a를 d만큼 할인해준다
for i in range(N):
    n = int(input())
    for j in range(n):
        sale[i].append(tuple(map(int, input().split())))
# print(sale)

order = permutations(range(N), N)   # index를 순열로 나타냄
# print(list(order))
ans = sum(origin)                   # 최대 비용을 구해두고 최소를 갱신한다
for case in order:
    cost = origin[:]                # 이 순서일 때의 가격
    tmp = 0                         # 이 순서일 때의 지불 비용
    for i in case:                  # 순서대로 순회하면서
        tmp += cost[i]              # 지불하고
        for a, d in sale[i]:        # 그 때 할인되는 것 확인
            cost[a - 1] -= d        # 할인하고
            if cost[a - 1] < 1:     # 1원보다 작으면 1원으로
                cost[a - 1] = 1
    ans = min(tmp, ans)             # 이때 지불 값으로 갱신

print(ans)
