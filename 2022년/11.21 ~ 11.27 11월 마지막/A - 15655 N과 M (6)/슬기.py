import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
tmp = []
def recur(cur, cnt):
    if cnt == m:
        print(*tmp)
        return

    if cur == n:
        return

    # for i in range(cnt, m):
    tmp.append(num[cur])
    recur(cur+1, cnt+1)
    tmp.pop()

    recur(cur+1, cnt)

recur(0, 0)