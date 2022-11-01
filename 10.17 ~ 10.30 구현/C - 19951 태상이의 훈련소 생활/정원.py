import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
acc = [0]*(N+1)
for m in range(M):
    a, b, k = map(int, input().rstrip().split())
    acc[a-1] += k
    acc[b] -= k
dp = [0]*(N+1)
dp[0] = acc[0]
for i in range(1, N+1):
    dp[i] = dp[i-1] + acc[i]
    print(arr[i-1] + dp[i-1], end=' ')

"""
누적합 배열인 acc를 생성한다
acc에는 누적합의 시작과 끝만 들어있으며
누적합이 시작될 때 k만큼 더했다가 끝나면서 k만큼 빼준다
현재 누적합은 변수로 가지고 있지는 않고
전에 계산한 누적합(dp[i-1])을 불러와서 acc[i]와 더한다
acc[i]가 0일 경우, 이전 누적합을 그대로 사용하며 그 값은 dp[i-1]에 같이 들어있다
해당 누적합이 종료되는 경우 k만큼 빼주어 해당 누적합을 종료한다
dp에 들어있는 값은 m줄 만큼 들어온 입력들의 누적합이며
이를 원 배열과 합한 결과를 출력한다
"""