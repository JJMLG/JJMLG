# 다시 풀 문제
import sys
sys.setrecursionlimit(10**6)
N = int(input())
trees = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
result = []
for i in range(N):
    try:
        x, y = map(int, input().split(' '))
        # if x ==1:
        #     trees[y].append(1)
        # elif y ==1:
        #     trees[x].append(1)
        # else:
        trees[x].append(y)
        trees[y].append(x)
    except:
        pass
# print(trees)
visited[1]=True

def findParent(start):
    for i in trees[start]:
        if visited[i] ==False:
            visited[i]=start
            findParent(i)

    # if trees[start]:
    #     for j in range(len(trees[start])):
    #         if visited[j]==1:
    #             pass
    #         else:
    #             visited[j]=1
    #             findParent(trees[start][j])
    # else:
    #     result.append(start)
    #     return
findParent(1)
# for i in range(1, N):
#     findParent(i)
for i in visited[2:]:
    print(i)
# record[i[0]] = [0]
# record = [0] *