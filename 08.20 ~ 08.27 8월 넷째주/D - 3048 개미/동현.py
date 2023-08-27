n,m = map(int,input().split())
ls1 = list(input())[::-1]
ls2 = list(input())
t = int(input())

ls = ls1 + ls2

dic = {}
for i in range(n):
    dic[ls1[i]] = 1
for i in range(m):
    dic[ls2[i]] = 0



while t >0:
    
    
     
    visited= [0]*(n+m)
    for i in range(n+m-1):
        if visited[i] == 0:
            if dic[ls[i]] == 1 and dic[ls[i+1]] == 0:
                ls[i+1],ls[i] = ls[i],ls[i+1]
                visited[i+1] = 1
          

   
   

    t -= 1
print("".join(ls))