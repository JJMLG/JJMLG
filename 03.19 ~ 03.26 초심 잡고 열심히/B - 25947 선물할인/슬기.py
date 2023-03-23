import sys
sys.stdin = open('input.txt')

n, b, a = map(int, input().split())
present = list(map(int, input().split()))
present.sort()

sale = 0
tmp = 0
cnt = 0
# idx = 0
for i in range(n):
    tmp += present[i]
    if tmp <= b:
        tmp += present[i]
        cnt += 1
    else:
        sale = 0
        print(i, tmp)
        for j in range(i):
            print(j)

        if sale == a:
            break
    print(cnt)