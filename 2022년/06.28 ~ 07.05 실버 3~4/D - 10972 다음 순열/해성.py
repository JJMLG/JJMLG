# import sys
# sys.stdin = open('input.txt')
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
# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
prev = list(map(int, input().split()))
makeNumber = list(range(1,N+1))
visited = [0 for _ in range(N)]
result = []
temp=[]
answer = []
now = 0
def dfs(start,temp):
    global result, now
    if len(temp) == N:
        result = temp[:]
        if now == 1:
            answer.append(temp[:])
            return answer
        elif result == prev:
            now = 1
            answer.append(temp[:])
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                temp.append(makeNumber[i])
                dfs(start+1, temp)
                temp.pop()
dfs(0, temp)
# if answer[0] == makeNumber[::-1]:
if makeNumber[::-1]:
    print(answer[0])
    print(-1)
else:
    print(*answer[1])