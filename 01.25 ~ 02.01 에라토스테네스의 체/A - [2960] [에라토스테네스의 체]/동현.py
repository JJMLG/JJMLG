import sys

n, k = map(int,input().split())

ls = [1]*(n+1)


start = 2
answer = 0
while True:
    cnt = 1
    if ls[start] == 0:
        start += 1
        continue
    while start*cnt <= n:
        if ls[start*cnt] == 1:
            ls[start*cnt] = 0
            answer += 1
            if answer == k:
                print(start*cnt)
                exit()
        cnt += 1

    start += 1

