import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())


for _ in range(m):
    u, v, b = list(map(int, input().split()))
    print(u, v, b)

k = int(input())
for _ in range(k):
    s, e = list(map(int, input().split()))
    print(s, e)