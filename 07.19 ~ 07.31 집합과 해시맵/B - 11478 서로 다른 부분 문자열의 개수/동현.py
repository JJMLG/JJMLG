import sys

a = input()
n = len(a)

i,j = 0,0
sett = set()
while i < n:
    if j == n:
        i += 1
        j = i
        continue
    
    sett.add(a[i:j+1])
    if j < n :
        j +=1 
    

print(len(sett))