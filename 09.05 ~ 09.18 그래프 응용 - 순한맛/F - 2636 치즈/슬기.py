import sys
sys.stdin = open('input.txt')

row, col = map(int, input().split())
# print(row, col)
plate = [list(map(int, input().split())) for _ in range(row)]

