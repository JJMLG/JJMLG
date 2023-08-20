
n,c,w = map(int,input().split())
ls = []
for _ in range(n):
    ls.append(int(input()))

ans = 0
maxx = max(ls)
for i in range(1,maxx+1):
    summ = 0
    for item in ls:
        if item % i != 0:
            cost = (item//i)*c
        else:
            cost = ((item//i)-1)*c
        temp = ((item//i)*w*i) - cost
        if temp < 0:
            continue
        summ += temp
    if summ > ans:
        ans = summ
print(ans)

        
    
