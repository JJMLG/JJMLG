import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
num = list(map(int, input().split()))

# num_index = list(range(1, len(num)+1))
# print(num_index)

dp = [0] * (n+10)


graph = [[] for _ in range(n+1)]
# print(graph)

for _ in range(m):
    i, w = list(map(int, input().split()))
    # print(i, w)
    graph[i].append(w)
print(graph[3][0])

dp[0] = 0
dp[1] = dp[1] + graph[1][0]
dp[2] = dp[1] + graph[2][0]
dp[3] = dp[2] + graph[3][0]
dp[4] = dp[3] + graph[4][0]
print(dp[3])

for i in range(len(graph)):
    print(i)
