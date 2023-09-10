import sys
import heapq
sys.stdin=open('input.txt')
from itertools import permutations
n = int(input())
prices = list(map(int,input().split()))
for i in range(n):
    m = int(input())
    for j in range(m):
        a,d = map(int,input().split())

ls = list(permutations(range(n),4))

for perm in ls:
    cost = 0
    price = prices[:]
    for i in range(len(perm)):
        cost += price[i]
        



# 순서 순열 구함
# 순서대로 할인 구매 가격 계산
