T = int(input())
k = int(input())

coin = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(k)]

dp = [[0 for _ in range(T+1)] for _ in range(k+1)] # 가로 세로 첫 줄은 0원
dp[0][0] = 1 # 0원을 만들 수 있는 경우는 1

for i in range(1, k+1): # 1번 동전, 2번 동전, i번 동전, ..., k번 동전
    val, cnt = coin[i] # 동전 가치, 동전 개수
    for cost in range(T+1): # 0원부터 T원까지, i번 동전을 사용하여 만들 수 있는 지 확인
        dp[i][cost] = dp[i-1][cost] # 앞서 i-1번 동전을 사용한 경우를 미리 불러오기
        for c in range(1, cnt+1): # val원의 동전 1개, 2개, c개, ..., cnt개
            if cost-c*val >= 0: # dp갱신 최소 조건
                dp[i][cost] += dp[i-1][cost-c*val] # i번 동전을 c개 사용하여 갱신할 수 있는 지점 확인
            else: # cost원을 i번 동전을 사용하여 갱신할 수 없을 경우에
                break

print(dp[k][T]) # k개 종류의 동전을 사용하여 T원을 만들 수 있는 경우 출력