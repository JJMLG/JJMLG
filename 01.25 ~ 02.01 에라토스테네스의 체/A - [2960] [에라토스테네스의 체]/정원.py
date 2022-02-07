N, K = map(int, input().split())

dp = [False, False] + [True] * (N-1)
cnt = 0

for i in range(2, N+1):
    if dp[i]:
        for j in range(i, N+1, i):
            if dp[j]:
                dp[j] = False
                cnt += 1
                if cnt == K:
                    print(j)
                    exit()
