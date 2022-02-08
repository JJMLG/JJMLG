N = int(input())
M = list(map(int,input().split()))


count = 0
for i in M:
    if int(i) == 1:
        count += 1
    else:
    
        for j in range(2,int(i)):
            if int(i) % j == 0:
                count += 1
                break

result=(N-count)
            

print(result)