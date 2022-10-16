import sys
def input():
    return sys.stdin.readline()

N = int(input())
cnt = 0
if N == 1 or N == 3:
    print(-1)
else:
    while N != 0:
        if not N%5:
            cnt += N//5
            break
        N -= 2
        cnt += 1
    print(cnt)