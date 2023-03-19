#2 4  1 3 5
t = int(input())
for _ in range(t):
    n = int(input())
    ls = []
    cnt = 0
    for i in range(n):
        a,b = map(int,input().split())
        ls.append([a,b])
    ls.sort()
  

    tmp = ls[0][1]
    for j in range(n):
        if ls[j][1] > tmp:
            cnt += 1
        if ls[j][1] < tmp:
            tmp = ls[j][1]
    print(n-cnt)
    