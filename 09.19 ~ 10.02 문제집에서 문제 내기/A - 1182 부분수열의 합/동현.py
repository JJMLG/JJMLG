
import sys
from collections import deque   
sys.stdin = open('input.txt')

import sys

n,m = map(int,input().split())
ls = list(map(int,input().split()))

temp = []
ans = 0
def dfs(start):
    global ans
    if temp:
        if sum(temp) == m:

            ans += 1


    for i in range(start,n):

        temp.append(ls[i])
        dfs(i+1)
        temp.pop()

dfs(0)
print(ans)