T = int(input())                        # 지폐 금액
k = int(input())                        # 동전 개수
coins = [list(map(int, input().split())) for _ in range(k)]

dp = [0] * (T + 1)                      # idx원을 만드는 방법은 v개
dp[0] = 1                               # 0원 만드는 방법은 1개

for coin, cnt in coins:
    for cost in range(T, 0, -1):        # cost 만드는 방법
        for n in range(1, cnt + 1):     # coin을 1개부터 cnt개까지 사용 가능
            if cost >= coin * n:
                dp[cost] = dp[cost] + dp[cost - (coin * n)]
            else:                       # n은 더 커지니까 그냥 stop
                break

print(dp[T])
