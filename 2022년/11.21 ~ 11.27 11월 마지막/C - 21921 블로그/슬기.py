import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
day = list(map(int, input().split()))

tmp = sum(day[:m])
ans = [tmp]

for i in range(m, n):
    tmp -= day[i-m]
    tmp += day[i]
    ans.append(tmp)

if sum(ans) == 0:
    print('SAD')
else:
    print(max(ans))
    print(ans.count(max(ans)))
