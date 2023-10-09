import sys
sys.stdin = open('input.txt')

n = int(input())
a = list(map(int, input().split()))
p, m, x, d = map(int, input().split())

maxx = -int(1e9)
minn = int(1e9)
# print(maxx)

def dfs(i, arr):
    global p, m, x, d, maxx, minn

    # 수열 다 봤을 경우 최댓값, 최솟값 계산
    if i == n:
        maxx = max(maxx, arr)
        minn = min(minn, arr)
    else:
        if p > 0:
            p -= 1
            dfs(i+1, arr + a[i])
            p += 1
        if m > 0:
            m -= 1
            dfs(i+1, arr - a[i])
            m += 1
        if x > 0:
            x -= 1
            dfs(i+1, arr * a[i])
            x += 1
        if d > 0:
            d -= 1
            dfs(i+1, int(arr/a[i]))
            d += 1

dfs(1, a[0])

print(maxx)
print(minn)