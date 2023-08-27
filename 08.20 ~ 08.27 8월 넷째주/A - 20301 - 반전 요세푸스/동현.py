import sys
from collections import deque

sys.stdin= open('input.txt')

n,k,m=map(int,input().split())

queue = deque(range(1,n+1))

idx = 0
result = []
while queue:
    for i in range(k-1) :
        queue.append(queue.popleft())
    result.append(queue.popleft())
    idx += 1
    if idx == m:
        queue = deque(reversed(queue))
        idx = 0

for i in result:
    print(i)