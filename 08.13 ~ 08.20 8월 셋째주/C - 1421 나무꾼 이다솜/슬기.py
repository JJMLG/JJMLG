import sys
sys.stdin = open('input.txt')

n, c, w = list(map(int, input().split()))

for _ in range(n):
    length = int(input())
    print(length)