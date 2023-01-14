def prime_list(size):
    sieve = [True]*(size+1)
    for i in range(2, int(size**0.5)+1):
        if sieve[i]:
            for j in range(i+i, size+1, i):
                sieve[j] = False
    return [i for i in range(2, size+1) if sieve[i]]

old, new = input().split()
new = int(new+old)
old = int(old)
primes = prime_list(int(1e7))
print('Yes' if old in primes and new in primes else 'No')