import sys
sys.stdin=open('input.txt')
from collections import deque
input = sys.stdin.readline


n = int(input())
m = int(input())
ls = list(input())

target = ['I','O','I']

ans = 0

# for i in range(len(ls)-len(target)+1):
i = 0
cnt = 0

while i < m - 1:

    if ls[i:i+3] == target:
        i += 2
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
        
    else:
        i += 1
        cnt = 0
print(ans)