dp = [False, False] + [True] * (999)
primes = []

for i in range(2, 1001):
    if dp[i]:
        primes.append(i)
        for j in range(i*2, 1001, i):
            dp[j] = False

N = int(input())
nums = list(map(int, input().split()))

maxx = nums[-1]
result = 0

for p in primes:
    for n in nums:
        if n == p:
            if n == 1:
                continue
            result += 1
    
    if p == maxx:
        break

print(result)