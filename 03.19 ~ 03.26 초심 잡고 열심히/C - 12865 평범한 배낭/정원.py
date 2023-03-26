N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0]*(K+1)
for item in items:
    weight, value = item
    for i in range(K, weight-1, -1): # top-down
        dp[i] = max(dp[i], dp[i-weight]+value)
print(dp[-1])

"""
top-down 방식의 문제이다
현재 무게(dp[i])에서 얻을 수 있는 가장 큰 가치를
아래 두 값 중 최대값으로 갱신한다
1. 이미 구한 현재 무게의 가치 최대치(dp[i])
2. 현재 물건의 무게만큼 더 담을 수 있던 시점의 가치 최대치에 현재 물건의 가치를 더한 값
ex) dp[7] = max(dp[7], dp[3]+items[4][value])
ex2) dp[6] = max(dp[6], dp[0]+items[6][value])
"""