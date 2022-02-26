import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

ls = [False, False] + [True] * (n-1)
primes = []
cnt = 0

for i in range(2, n+1):
    if ls[i]:
        primes.append(i)
        for j in range(i, n+1, i):
            ls[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                exit()