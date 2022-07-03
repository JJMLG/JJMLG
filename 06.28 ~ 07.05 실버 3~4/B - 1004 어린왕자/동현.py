
t = int(input())
for i in range(t):
    cnt = 0
    startX,startY,endX,endY = map(int,input().split())

    n = int(input())
    ls = []
    for i in range(n):
        x,y,r = map(int,input().split())
        dis = ((x-startX)**2+(y-startY)**2)**(1/2)
        dis_2 =  ((x-endX)**2+(y-endY)**2)**(1/2)

        if dis <= r and dis_2 <=r:
            continue
        if dis <= r or dis_2 <=r:
            cnt += 1


        

    print(cnt)