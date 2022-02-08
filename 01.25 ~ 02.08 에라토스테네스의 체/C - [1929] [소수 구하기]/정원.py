M, N = map(int, input().split())

# 소수인지 확인할 DP배열
dp = [False, False] + [True] * (N-1)

primes = [] # 소수를 구해서 담을 리스트

for i in range(2, N+1):
    if dp[i]: # 2부터 시작, 소수를 찾았다??
        primes.append(i) # 소수 리스트에 추가
        for j in range(i*2, N+1, i): 
            # i의 배수는 전부 소수가 아님
            if dp[j]: # 최적화
                dp[j] = False

for p in primes: # N까지 구한 소수들 중에서
    if p >= M: # M보다 큰 소수다?
        print(p) # 출력