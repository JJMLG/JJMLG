import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
k = int(input())

for _ in range(k):
    r, c, d = map(int, input().split())