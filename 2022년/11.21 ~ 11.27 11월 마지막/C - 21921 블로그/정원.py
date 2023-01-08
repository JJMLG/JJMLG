import sys

input = sys.stdin.readline

N, X = map(int, input().rstrip().split())
visitors = list(map(int, input().rstrip().split()))

tmp = sum(visitors[:X])
maxx = tmp
cnt = 1

for i in range(X, N):
    tmp -= visitors[i-X]
    tmp += visitors[i]
    if maxx < tmp:
        maxx, cnt = tmp, 1
    elif maxx == tmp:
        cnt += 1

print('SAD') if not maxx else print(maxx, cnt)