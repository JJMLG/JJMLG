import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
coins = [int(input().rstrip()) for _ in range(N)]
dp = [0]*(K+1)
dp[0] = 1 # 0원을 지불하는 방법은, 아무것도 내지 않는 경우 딱 하나
for coin in coins: # 각각 동전 종류에 대해
    for i in range(1, K+1): # 1원을 내는 경우부터 출발
        if i-coin>=0: # 음수의 금액을 낸 경우는 존재하지 않으므로, 0원을 낸 경우 이상부터 확인
            dp[i] += dp[i-coin] # 해당 금액의 동전을 내기 전의 경우의 수 만큼을 더해준다
print(dp[K])

"""
예제는 동전의 종류가 1 2 5 이므로 1원동전 일 때, dp가 1, 1, 1, ... 이 되기 때문에 헷갈릴 수 있으나
만약 2 5 7과 같은 종류였다면
for coin in coins 1회차에 dp는 
1, 0, 1, 0, 1, 0, 1 ... 과 같이 저장되었을 것이다
계산된 값(dp[i])를 실시간으로 반영하면서 line 10의 for문을 돌기 때문에
dp[i] += dp[i-coin] 만으로도 정답코드가 될 수 있다
"""

# https://www.acmicpc.net/problem/2293