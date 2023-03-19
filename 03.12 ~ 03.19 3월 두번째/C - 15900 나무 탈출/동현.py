import sys

sys.setrecursionlimit(30000)
input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    for i in arr[start]:
        if visited[i] == 0:
            temp[i] = temp[start] + 1
            dfs(i)



n = int(input())
arr = [[]*(n+1) for _ in range(n+1)]
visited = [0] * (n + 1)
temp = [0] * (n+1)
cnt = 0
for i in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(1)

for j in range(2,n+1):
    if len(arr[j]) == 1:
        cnt += temp[j]

# print(cnt)
# print(arr)
# print(visited)
# print(temp)
if cnt % 2 == 0:
    print('No')

else:
    print('Yes')