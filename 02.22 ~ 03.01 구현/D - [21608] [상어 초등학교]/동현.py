import sys


def find(f1,f2,f3,f4,vacancy):
    global a,b,c,d,count,x,y
    max_friend = 0
    max_vacancy = 0
    for i in range(n):
        for j in range(n):
            count = 0
            count_2 = 0

            if i == 0:
                a = 0
            else:
                a = arr[i-1][j]
                if a == 0:
                    count_2 += 1
                if a == f1 or a == f2 or a == f3 or a == f4:
                    count += 1
            if j == 0:
                b  = 0
            else:
                b = arr[i][j-1]
                if b == 0:
                    count_2 += 1
                if b == f1 or b == f2 or b == f3 or b == f4:
                    count += 1
            if i == n-1:
                c = 0
            else:
                c = arr[i+1][j]
                if c == 0:
                    count_2 += 1

                if c == f1 or c == f2 or c == f3 or c == f4:
                    count += 1
            if j == n-1:
                d = 0
            else:
                d = arr[i][j+1]
                if d == 0:
                    count_2 += 1

                if d == f1 or d == f2 or d == f3 or d == f4:
                    count += 1



            if count > max_friend:
                if arr[i][j] == 0:
                    vacancy = []
                    max_friend = count
                    x, y, cnt = i, j, count_2

            if count == max_friend:
                if arr[i][j] == 0:
                    vacancy.append((i,j,count_2))

    vacancy.sort(key=lambda x: (-x[2],x[0],x[1]))
    x,y,cnt = vacancy[0]
    return x,y,cnt


n = int(input())
arr = [[0]*n for _ in range(n)]
dic = {}
for i in range(n**2):
    me,f1,f2,f3,f4 = map(int,input().split())
    dic[me] = [f1,f2,f3,f4]
    if i == 0:
        arr[1][1] = me
        continue
    vacancy = []
    ls = find(f1,f2,f3,f4,vacancy)

    arr[ls[0]][ls[1]] = me


summ = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        if i == 0:
            q = 0
        else:
            q = arr[i-1][j]
            if q in dic[arr[i][j]]:
                cnt +=1

        if i == n-1:
            w = 0
        else:
            w = arr[i+1][j]
            if w in dic[arr[i][j]]:
                cnt +=1

        if j == 0:
            e = 0
        else:
            e = arr[i][j-1]
            if e in dic[arr[i][j]]:
                cnt +=1

        if j == n-1:
            r = 0
        else:
            r = arr[i][j+1]
            if r in dic[arr[i][j]]:
                cnt +=1

        if cnt == 0:
            summ += 0
        elif cnt == 1:
            summ +=1
        elif cnt == 2:
            summ += 10
        elif cnt == 3:
            summ += 100
        elif cnt == 4:
            summ += 1000


print(summ)
