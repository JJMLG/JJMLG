from itertools import combinations
n = int(input())
ls_1 = []
ls_2 = []
for _ in range(n):
    s,b = map(int,input().split())
    ls_1.append(s)
    ls_2.append(b)

maxx = 987654321
for i in range(1,n+1):
    
    for j in list(combinations(range(n),i)):
        tempS = 1
        tempB = 0
        for k in j:
            tempS *= ls_1[k]
            tempB += ls_2[k]
        if abs(tempS-tempB) < maxx:
            maxx = abs(tempS-tempB)
            

print(maxx)


