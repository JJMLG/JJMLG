import sys
sys.stdin = open("21608.txt")

N = int(input())

record = [[0]* N for _ in range(N)]
# print(record)
fav = [list(map(int, input().split()))for _ in range(N**2)]
favlist = [0] * (N**2+1)
studentList = []
# 학생 번호 리스트 studentList
# 학생이 좋아하는 학생 번호리스트를 학생의 인덱스에 담아줌 favlist, 1번학생이 좋아하는 학생리스트는 1번째 인덱스에
idx = 0
for i in range(N**2):
    studentList.append(fav[i][0])
    favlist[fav[i][0]]=fav[i][1:]
# print(studentList)
# print(favlist)
#  우 하 좌 상
Y=[0, 1, 0, -1]
X=[1, 0, -1, 0]
# 학생번호하나씩 꺼내서
for stu_Num in studentList:
    # 비어있는 칸중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
    max_like_count = -1
    max_vacant_count = -1
    temp = []
    for y in range(N):
        for x in range(N):
            if record[y][x] == 0:
                like_count = 0
                vacant_count=0
                for idx in range(4):
                    dx = x + X[idx]
                    dy = y + Y[idx]
                    # if dy>=0 and dy<= N-1:
                    if dy < 0 or dy > N-1 or dx < 0 or dx > N-1:
                        pass
                    else:
                        # print(dy, dx)
                        if record[dy][dx] in favlist[stu_Num]:
                            like_count +=1
                        # print(like_count)
                        if record[dy][dx] == 0:
                            vacant_count +=1
                if max_like_count < like_count:
                    # print(1)
                    max_like_count = like_count
                    max_vacant_count = vacant_count
                    temp = [y,x]
                elif max_like_count == like_count:
                    if vacant_count > max_vacant_count:
                        max_vacant_count = vacant_count
                        temp =[y,x]
    record[temp[0]][temp[1]] = stu_Num

result = 0
for i in range(N):
    for j in range(N):
        tempcount = 0
        for idx in range(4):
            dy = i + Y[idx]
            dx = j + X[idx]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1:
                pass
            else:
                # print(record[dy][dx])
                if record[dy][dx] in favlist[record[i][j]]:
                    # print(1)
                    tempcount += 1
        if tempcount < 1:
            tempcount = 0
        else:
            result += 10**(tempcount-1)
print(result)
