import sys
sys.stdin=open('input.txt')
# 상하좌우
N = int(input())
visited = [[0 for _ in range(N)] for _ in range(N)]
maps = [list(map(int, input())) for _ in range(N)]
Y = [-1, 0, 1, 0]
X =[0, 1, 0, -1]
count = 0
record = 0
numberOfHouse = []
# print(visited)
# print(maps)
maxCount=0
def dfs(y,x, count):
    global record
    # 방문안해도 되는 곳이면 패스
    if maps[y][x] == 0:
        return
    else:
        visited[y][x]=count
        record +=1
        #     return
        # # if maps[y][x] ==0:
        #     numberOfHouse.append(record)
        #     return
        # else:
        for i in range(4):
            dy = y + Y[i]
            dx = x + X[i]
            # 다음 넘겨줄게 영역 밖이거나, 방문한 곳이라면 패스
            if dy<0 or dx <0 or dx>N-1 or dy > N-1 or visited[dy][dx] !=0:
                pass
            else:
                dfs(dy, dx, count)
    # print(maxCount)
for i in range(N):
    for j in range(N):
        if maps[i][j] ==1 and visited[i][j] ==0:
            count +=1
            dfs(i,j, count)
            numberOfHouse.append(record)
            record = 0
# for i in range(count):

print(count)
for i in sorted(numberOfHouse):
    print(i)
