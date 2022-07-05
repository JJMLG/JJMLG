import sys
sys.stdin = open('input.txt')
# from itertools import permutations
# N = int(input())
# makeNumber = list(range(1,N+1))
# prev = tuple(list(map(int, input().split())))
#
# a = list(permutations(makeNumber, N))
# if a.index(prev) == len(a)-1:
#     print(-1)
# else:
#     print(*a[a.index(prev)+1])
# ----------------------------------------
sys.setrecursionlimit(100000)
N = int(input())
prev = list(map(int, input().split()))
makeNumber = list(range(1,N+1))
visited = [0 for _ in range(N)]
result = []
temp=[]
def dfs(start,temp):
    global result
    if len(temp) == N:
            result = temp[:]
        # return result
        # temp = []
        # temp = []
        # return result
        # temp = []
        # return temp
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                temp.append(makeNumber[i])
                dfs(start+1, temp)
                # temp = []
                temp.pop()
                visited[i] = 0
    # return result
    # return result
dfs(0, temp)

if result == makeNumber[::-1]:
    print(-1)
else:
    print(*result)
    # for i in makeNumber:
        # if visited[i]
