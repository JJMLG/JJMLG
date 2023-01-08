import sys

n = int(input())
ls = sorted(list(map(int,input().split())))
tot = int(input())



start, end = 0, ls[-1]

while start <= end:
    mid = (start + end) // 2

    budget = 0
    for i in range(n):
        if ls[i] >= mid:
            budget += mid
        else:
            budget += ls[i]
    
    if budget <= tot:
        start = mid + 1
    else:
        end = mid - 1

print(end)

