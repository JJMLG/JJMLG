M, N = map(int, input().split())

dp = [False, False] + [True] * (N-1)

primes = []

for i in range(2, N+1):
    if dp[i]:
        primes.append(i)
        for j in range(i*2, N+1, i):
            if dp[j]:
                dp[j] = False

for p in primes:
    if p >= M:
        print(p)