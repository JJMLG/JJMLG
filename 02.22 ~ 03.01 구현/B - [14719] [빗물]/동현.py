import sys


h, w = map(int,input().split())
ls = list(map(int,input().split()))
val = 0
for i in range(1,w-1):
    left_max = max(ls[0:i])
    right_max = max(ls[i+1:w])

    if min(left_max,right_max) >= ls[i]:
        val += min(left_max,right_max) - ls[i]

print(val)