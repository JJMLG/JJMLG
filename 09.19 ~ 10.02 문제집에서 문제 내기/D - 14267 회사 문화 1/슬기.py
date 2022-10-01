import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
num = list(map(int, input().split()))

for _ in range(m):
    i, w = list(map(int, input().split()))
    # print(i, w)