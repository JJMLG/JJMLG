import sys
sys.stdin = open('input.txt')

n = int(input())
name = input()
old = [input() for _ in range(n)]
print(old)
s_old = old
visited = [0] * (len(old)+1)
cnt = 0

for j in name:
    for i in old:
        pass
