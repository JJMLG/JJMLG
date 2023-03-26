import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

stuff = [[0, 0]]
arr = [[0] * (k+1) for _ in range(n+1)]
for _ in range(n):
    w, v = map(int, input().split())
    stuff.append([w, v])

for i in range(1, n+1):
    for j in range(1, k+1):
        w = stuff[i][0]
        v = stuff[i][1]

        if j < w:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j], v + arr[i-1][j-w])
print(arr[n][k])