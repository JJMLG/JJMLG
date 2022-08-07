import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
time = [int(input()) for _ in range(n)]
# print(time)

# for _ in range(n):
#     time = int(input())