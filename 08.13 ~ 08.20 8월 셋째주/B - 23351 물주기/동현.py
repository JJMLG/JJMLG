import sys


n,k,a,b= map(int,input().split())

ls = [k]*n
ans = 0
while True:
    if 0 in ls:
        print(ans)
        break
    for i in range(a):
        ls[ls.index(min(ls))] += b
    for j in range(n):
        ls[j] -= 1
    ans += 1


        
    
