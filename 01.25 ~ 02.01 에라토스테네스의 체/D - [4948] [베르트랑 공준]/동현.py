import sys

ls = [0]*(2*123456+1)
ls[1] =1
for i in range(2,len(ls)):
    cnt = 2
    while i*cnt < 123456*2+1:
        ls[i*cnt] = 1
        cnt += 1

while True:
    n = int(input())
    if n == 0:
        break
    summ = 0
    for j in range(n+1,2*n+1):
        if ls[j] == 0:
            summ += 1

    print(summ)
