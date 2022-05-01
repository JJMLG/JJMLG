import sys
sys.stdin = open('input.txt')

board = int(input())

arr = [list(map(str, input())) for _ in range(board)]
print(arr)

