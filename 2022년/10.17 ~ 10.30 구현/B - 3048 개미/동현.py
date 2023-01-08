import sys

n,m = map(int,input().split())
a = list(input())
b= list(input())[::-1]
t = int(input())
cnt = 0 
aCheck = [1]*n
bCheck = [-1] *m
ls = aCheck + bCheck

while cnt != t:
    visited = [0]*(n+m+1)
    for i in range(n+m):
        if visited[i] == 0:
            if ls[i] == 1 and ls[i+1] == -1:
                visited[i]= -1
                visited[i+1] = 1
            else:
                visited[i] = ls[i]

    cnt += 1
    ls = visited
   

result = ''
for k in range(n+m):
    if ls[k] == -1:
        result += b.pop()
    else:
        result += a.pop()
print(result)