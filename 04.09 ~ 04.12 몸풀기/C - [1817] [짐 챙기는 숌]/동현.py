import sys

n, m = map(int,input().split())
if n == 0:
    print(0)
else:
    ls = list(map(int,input().split()))

    result = 0
    tmp = 0
    for i in range(n):
        if tmp + ls[i] < m:
            tmp += ls[i]
            if i == len(ls)-1:
                result +=1

        elif tmp + ls[i] == m:
            tmp = 0
            result += 1

        else:
            result += 1
            tmp = ls[i]
            if i == len(ls)-1:
                result +=1


    print(result)
