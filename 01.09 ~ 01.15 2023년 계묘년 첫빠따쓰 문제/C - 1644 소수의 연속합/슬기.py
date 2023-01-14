import sys
sys.stdin = open('input.txt')

n = int(input())

arr = [True] * (n+1)
arr[0], arr[1] = 0, 0

prime = []
for i in range(2, n+1):
    if arr[i]:
        prime.append(i)
        for j in range(i+i, n+1, i):
            arr[j] = False


s = 0
e = 0

res = 0

while e <= len(prime):
    tmp = sum(prime[s:e])
    if tmp == n:
        res += 1
        e += 1
    elif tmp < n:
        e += 1
    else:
        s += 1

print(res)