import sys
sys.stdin = open('input.txt')

n, m, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)