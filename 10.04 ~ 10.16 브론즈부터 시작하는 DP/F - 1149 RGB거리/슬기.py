import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


color = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j])
        if arr[i][j]:
            pass