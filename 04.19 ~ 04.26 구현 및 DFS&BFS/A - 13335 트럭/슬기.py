import sys
sys.stdin = open('input.txt')

truck, bridge, maxweight = map(int, input().split())
weight = list(map(int, input().split()))
# print(weight)

# 두 대가 동시에 지나갈 수도 있음