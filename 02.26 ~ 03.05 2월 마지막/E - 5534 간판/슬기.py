import sys
sys.stdin = open('input.txt')

n = int(input())
name = input()
old = [input() for _ in range(n)]
print(old)
s_old = old
visited = [0] * (len(old)+1)
cnt = 0

for i in old:
    if i == name:
       cnt += 1

idx = 0
for i in name:
    for j in old:
        pass