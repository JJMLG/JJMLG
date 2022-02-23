import sys

n = int(input())
rome = [1,5,10,50]
ls = []
sum_ls = [0] * 1001

def dfs(depth,num):

    if depth == n:
        sum_ls[sum(ls)] =1
        return

    for i in range(num,4):
        ls.append(rome[i])
        dfs(depth +1, i)
        ls.pop()


dfs(0,0)
print(sum(sum_ls))