N = int(input())
conference = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)
dp[1] = conference[0][2]

for i in range(2, N + 1):
    dp[i] = max(dp[i - 2] + conference[i - 1][2], dp[i - 1])

print(dp[-1])


# # 브루투포스
# ans = 0
# def recur(idx, cnt):
#     global ans
#     if idx + 2 >= N:
#         if cnt > ans:
#             ans = cnt
#         return

#     for i in range(idx + 2, N):
#         recur(i, cnt + conference[i][2])

# for i in range(N):
#     recur(i, conference[i][2])

# print(ans)
