N, K = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = arr[i]
    for j in range(1, K + 1):
        if w > j:                                                   # 지금 넣고싶은 물건의 무게(w)가 지금 배낭의 허용 무게(j)보다 무거우면
            dp[i][j] = dp[i - 1][j]                                 # 못 넣으니까 이전 배낭
        else:                                                       # 지금 물건 넣을 수 있으면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)      # 이전 배낭 vs 현재 물건무게만큼 배낭에서 빼고 현재 물건 넣기
        
        # dp[i][j] = dp[i - 1][j] if w > j else max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])

# dp
# [0, 0, 0, 0, 0,  0,  0,  0]
# [0, 0, 0, 0, 0,  0, 13, 13] 
# [0, 0, 0, 0, 8,  8, 13, 13] 
# [0, 0, 0, 6, 8,  8, 13, 14] 
# [0, 0, 0, 6, 8, 12, 13, 14]
