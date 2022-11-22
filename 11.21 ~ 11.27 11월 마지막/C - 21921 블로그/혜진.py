N, X = map(int, input().split())
lst = list(map(int, input().split()))

ans, cnt = sum(lst[0:X]), 1
sub = ans
for i in range(N - X):
    sub = sub - lst[i] + lst[i + X]
    if sub > ans:
        ans = sub
        cnt = 1
    elif sub == ans:
        cnt += 1

if ans:
    print(ans)
    print(cnt)
else:
    print("SAD")
