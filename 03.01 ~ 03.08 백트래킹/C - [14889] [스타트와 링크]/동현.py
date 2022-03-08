import sys
sys.stdin=open('input.txt')



def dfs(start):
    if len(s) == n/2:
        copy_s = s[:]
        result.append(copy_s)
        result_2.append(list(set(case)-set(copy_s)))
        return

    for j in range(start, n):
        s.append(j)
        dfs(j+1)
        s.pop()



n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
s = []
result = []
result_2 = []
case = list(range(n))
for i in range(n):
    for j in range(n):
        if i < j:
            arr[i][j] += arr[j][i]


dfs(0)

minn = 987654321
for i in range(len(result)):
    start_sum = 0
    link_sum = 0
    for j in range((n//2)-1):
        for k in range(j+1,n//2):
            start_sum += arr[result[i][j]][result[i][k]]
            link_sum += arr[result_2[i][j]][result_2[i][k]]
    diff = abs(start_sum - link_sum)

    if diff <= minn:
        minn = diff

print(minn)