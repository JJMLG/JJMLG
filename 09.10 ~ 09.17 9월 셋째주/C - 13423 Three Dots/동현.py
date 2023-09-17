t = int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int,input().split()))
    ls.sort()
    ans = 0
    dict = {}
    for i in range(n):
        dict[ls[i]] = 1
    for i in range(n-1):
        for j in range(i+1,n):
            # if 2*ls[j] - ls[i] > n-1:
            #     break
           
            if 2*ls[j] - ls[i] in dict:
                ans += 1
        
    print(ans)
