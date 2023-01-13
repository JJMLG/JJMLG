old, new = input().split()
new = int(new + old)
old = int(old)

isprime = [1] * (new + 1)
isprime[0], isprime[1] = 0, 0

for i in range(2, int(new ** 0.5) + 1):
    if not isprime[i]: continue
    for j in range(i + i, new + 1, i):
        if isprime[j]: isprime[j] = 0

print('Yes' if isprime[old] and isprime[new] else 'No')
