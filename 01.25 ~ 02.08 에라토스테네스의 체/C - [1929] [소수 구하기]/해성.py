# import sys

M, N =map(int,input().split())
if M==1:
    M=2
    arr = list(range(M, N+1))
elif M>1:
    arr = list(range(M, N+1))

# mins=arr[0]
result=[]
for i in range(len(arr)):
    # 0 13
    # print(i)
    cnt = 0
    for j in list(range(arr[i])):
                # print(arr[j])
        if j!=0 and j!=1 and arr[i] != 1000001 and arr[i] % j == 0:
            arr[i] =1000001
            break
        if j!= 0 and j!=1 and arr[i] != 1000001 and arr[i] % j !=0:
            cnt +=1
            if cnt == j:
                result.append(arr[i])
            # arr[i]=1000001
# print(arr)
for i in arr:
    if i != 1000001:
        print(i)



