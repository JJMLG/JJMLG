import sys

N , K = map(int, input().split())

sn = 2
arr = list(range(2,N+1))

cnt=0
result=0
sosu = arr[0]
while cnt < K:
    sosu = min(arr)

    for i in range(len(arr)):
        # 1001이 문제 최대보다 크니까
        if arr[i] != 1001 and arr[i] % sosu == 0:
            cnt += 1
            arr[i] = 1001
        if cnt == K:
            result = i
            break
        else:
            pass
    # print(arr)
print(result+2)


