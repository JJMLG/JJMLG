import sys
sys.stdin = open('input.txt')

n, b, a = map(int, input().split())
present = list(map(int, input().split()))
present.sort()
visited = [0] * n
tmp = 0
cnt = 0
# idx = 0
for i in range(n):
    if (tmp + present[i]) <= b:
        tmp += present[i]
        cnt = i + 1
    else:
        flag = 0
        for j in range(i, -1, -1):
            if visited[j]:
                continue
            if a == 0:
                break
            tmp -= present[j] // 2
            a -= 1
            visited[j] = 1
            if (tmp + present[i]) <= b:
                flag = 1
                tmp += present[i]
                cnt = i + 1
                break

        if flag == 0:
            break
print(cnt)