import sys

n = int(input())
ls = sorted(list(map(int,input().split())))
m = int(input())
ls_2 = list(map(int,input().split()))

dict = {}

for i in ls:
    if i in dict:
        dict[i] +=1 
    else:
        dict[i] = 1


result = []

for target in ls_2:
    flag = 0
    start,end = 0, len(ls) - 1
    while start <= end:
        
        mid = (start + end) // 2

        if ls[mid] == target:
            flag = 1
            
            break
        if ls[mid] < target:
            start = mid + 1
            
        else:
            end = mid - 1
    
    if flag == 0:
        result.append(0)
    else:
        result.append(dict[target])
    # result.append(cnt)

print(*result)