def prime_list(size):
    sieve = [True]*(size+1)
    for i in range(2, int(size**0.5)+1):
        if sieve[i]:
            for j in range(i+i, size+1, i):
                sieve[j] = False
    return [i for i in range(2, size+1) if sieve[i]]

N = int(input())
if N == 1: 
    print(0)
else:
    primes = prime_list(N)
    s, e, now = 0, 0, primes[0]
    max_len = len(primes)-1
    result = 0

    while 1:
        if (now < N and e == max_len) or (now > N and s == max_len): 
            break

        if now == N: result += 1

        if now < N:
            e += 1
            now += primes[e]
        else:
            now -= primes[s]
            s += 1

    print(result)