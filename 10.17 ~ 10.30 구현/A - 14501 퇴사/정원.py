import sys

input = sys.stdin.readline

N = int(input().rstrip())
T, P = [], []
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    T.append(a)
    P.append(b)
dp = P[:] + [0] # 최대 수익을 동적으로 기록할 DP테이블
for i in range(N-1, -1, -1): # Top-Down
    if T[i]+i > N: dp[i] = dp[i+1]
    else: dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
print(dp[0])

"""
i일에 시작한 일이 근무일을 넘길 경우
해당 일은 처리할 수 없고
그 다음날의 일 처리량과 동일하다
반대로 근무일 안에 끝낼 수 있을 경우
그 일을 할 수도 있고 안 할 수도 있는데
안 할 경우는 dp[i+1]
할 경우는 P[i] + dp[i+T[i]]

안 할 경우에 dp[i+1]인 이유는
그 일을 하지 않았기 때문에 dp[i]의 일 처리량과 
하지 않고 넘어간 다음날인 dp[i+1]의 일 처리량이 동일하다
일을 할 경우 P[i]는 일 처리량이고
dp[i+T[i]]는 
일 처리에 필요한 시간이 경과한 날의 일 처리량이 된다
이 경우 시간 안에 일 처리가 가능하므로 
P[i]의 일 처리량을 dp[i+T[i]]에 얹은 값을 계산한다
그리고 이 둘의 크기를 비교하여 큰 값을 최대 일처리량으로 기록하면서
위에서부터 내려오는 Top Down 방식으로 값들을 계산하는 DP문제이다
"""