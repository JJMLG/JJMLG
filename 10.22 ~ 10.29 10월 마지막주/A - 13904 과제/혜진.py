N = int(input())
ans = maxday = 0

Q = []
for _ in range(N):
    d, w = map(int, input().split())
    Q.append([d, w])
    maxday = max(maxday, d)
Q.sort(key=lambda x:(-x[1], x[0]))
work = [False] * (maxday + 1)

for d, w in Q:
    for i in range(d, 0, -1):
        if work[i]: continue
        work[i] = True
        ans += w
        break
print(ans)
