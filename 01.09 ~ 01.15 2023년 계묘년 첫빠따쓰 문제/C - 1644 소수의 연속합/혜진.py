N = int(input())

# 1인 경우 예외처리 안해줘서 자꾸 틀림
if N == 1:
    print(0)
    exit()

# 소수인지 판별
isprime = [1 for _ in range(N + 1)]
isprime[0], isprime[1] = 0, 0
for i in range(2, int(N ** 0.5) + 1):
    if not isprime[i]: continue
    for j in range(i + i, N + 1, i):
        if isprime[j]: isprime[j] = 0

# 소수인 수 배열
prime = [i for i in range(2, N + 1) if isprime[i]]

s, e, ans = 0, 0, 0
sub = prime[0]
while True:
    # 너무 크면
    if sub > N:
        sub -= prime[s]
        s += 1
    else:
        # 같으면 ans + 1 and 작으면
        if sub == N:
            ans += 1
        e += 1
        if e < len(prime):
            sub += prime[e]
        else:
            break

print(ans)
