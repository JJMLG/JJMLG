import sys

N = int(input())
arr = list(map(int,input().split()))

cnt=0
for i in arr:
    temp=0
    if i ==1:
        pass
    else:
        for j in list(range(1,i)):
            if j ==1:
                pass
            elif i%j== 0:
                break
            else:
                temp+=1
        if temp == j-1:
            cnt+=1
print(cnt)


