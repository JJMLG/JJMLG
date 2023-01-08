import sys
sys.stdin = open('input.txt')

n, x, y = map(int, input().split())
arr = [0] * (2*n+1)
arr[x] = arr[y] = y-x-1
# print(arr)
res = 0
def dfs(depth):
    global res
    if depth == (y-x-1):
        dfs(depth + 1)

    if depth == n+1:
        res += 1
        # print(arr)
        return

    for i in range(1, len(arr) - depth - 1):
        if arr[i] == 0 and arr[i+depth+1] == 0:
            arr[i] = arr[i+depth+1] = depth
            dfs(depth+1)
            arr[i] = arr[i+depth+1] = 0

dfs(1)
print(res)