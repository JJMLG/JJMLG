import sys
sys.stdin = open("15649.txt")
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
# print(N, M)
numlist = list(range(1, N+1))
# print(numlist)
madelist = []
result = []
visited = [0 for _ in range(N+1)]
# print(visited)
def back(madelist):
    if len(madelist) == M:
        temp = madelist.copy()
        result.append(temp)
        # return result
    else:
        for i in numlist:
            if visited[i] == 1:
                continue
            else:
                visited[i] = 1
                madelist.append(i)
                back(madelist)
                madelist.pop()
                visited[i] = 0
    return result

back(madelist)

for i in result:
    print(*i)
