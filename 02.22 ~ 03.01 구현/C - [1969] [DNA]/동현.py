import sys
sys.stdin=open('input.txt')

n, m = map(int,input().split())
ls = []
for _ in range(m):
    ls.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})


for i in range(n):
    a = input()
    for j in range(m):
        if a[j] == 'T':
            ls[j]['T'] += 1
        elif a[j] == 'A':
            ls[j]['A'] += 1
        elif a[j] == 'C':
            ls[j]['C'] += 1
        elif a[j] == 'G':
            ls[j]['G'] += 1

diff = 0
result = ''
for j in range(len(ls)):
    maxx = max(ls[j], key=ls[j].get)
    result += maxx
    diff += sum(ls[j].values()) - ls[j][maxx]

print(result)
print(diff)