import sys
sys.stdin = open('input.txt')
from itertools import combinations

n, s = map(int, input().split())
ls = list(map(int, input().split()))

cnt = 0

for i in range(1, n+1):
    comb = combinations(ls, i)

    for j in comb:
        if sum(j) == s:
            cnt += 1
print(cnt)


# def dfs(idx, hap):
#     global cnt
#
#     if idx >= n:
#         return
#
#     hap += ls[idx]
#
#     if hap == s:
#         cnt += 1
#
#     dfs(idx + 1, hap - ls[idx])
#
#     dfs(idx + 1, hap)
#
# dfs(0, 0)
# print(cnt)