import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    print(a, b)