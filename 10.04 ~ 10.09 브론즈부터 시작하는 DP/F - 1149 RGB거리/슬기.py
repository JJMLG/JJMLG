import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)