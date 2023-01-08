import sys

n, m = map(int,input().split())

if n == 1:
    print(1)



elif n == 2:
    if m < 9 :
        print((m-1)//2+1)

    else:
        print(4)

else:
    if m < 7:
        print(min(4,m))
    else:
        print(m-2)



