import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
tall = list(map(int, input().split()))

jo = [0] * (k+1)
# print(jo)
for _ in range(n):
    pass