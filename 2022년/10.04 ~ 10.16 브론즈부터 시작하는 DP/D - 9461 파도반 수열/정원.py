dp = [1, 1, 1, 2, 2, 3] + [0]*97
for i in range(5, 103): 
    dp[i] = dp[i-5]+dp[i-1]
for _ in range(int(input())): 
    print(dp[int(input())-1])