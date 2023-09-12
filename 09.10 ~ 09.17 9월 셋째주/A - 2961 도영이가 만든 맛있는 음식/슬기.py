from itertools import combinations
from functools import reduce

n = int(input())

sour = []
bit = []
for _ in range(n):
    s, b = map(int, input().split())
    sour.append(s)
    bit.append(b)

gap = int(1e9)
ss = []
for i in range(1, n+1):
    for j in combinations(sour, i):
        ss.append(reduce(lambda x, y: x*y, j))

bb = []
for i in range(1, n+1):
    for j in combinations(bit, i):
        bb.append(sum(j))

for i in range(len(ss)):
    if gap > abs(ss[i] - bb[i]):
        gap = abs(ss[i] - bb[i])
print(gap)