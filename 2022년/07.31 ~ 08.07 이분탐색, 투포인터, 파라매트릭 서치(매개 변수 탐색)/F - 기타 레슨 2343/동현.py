import sys

sys.stdin=open('input.txt')

n, m = map(int,input().split())
ls = list(map(int,input().split()))

start, end = 0, 10000000000
result = sum(ls)



while start <= end:
    mid = (start + end) // 2
    if mid < max(ls):
        start = mid + 1
        continue

    cnt = 1
    tmp = 0

    for i in range(n):
        if tmp + ls[i] <= mid:
            tmp += ls[i]
        else:
            tmp = ls[i]
            cnt += 1
    
    if cnt <= m:
        end = mid - 1
        result = min(result,mid)
    else:
        start = mid +1 

print(result)