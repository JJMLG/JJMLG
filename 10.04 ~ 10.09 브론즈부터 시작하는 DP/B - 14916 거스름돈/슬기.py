import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

n = int(input())

cnt = 0
i = 0

while True:
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 2
        cnt += 1

    if n < 0:
        break

if n < 0:
    print(-1)
else:
    print(cnt)

