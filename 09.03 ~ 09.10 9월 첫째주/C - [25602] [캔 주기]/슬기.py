import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
a = list(map(int, input().split()))

r = []
m = []
for _ in range(k):
    r.append(list(map(int, input().split())))
# print(r)
for _ in range(k):
    m.append(list(map(int, input().split())))

tmp = 0
hap = 0
visited = [0] * (n+10)
print(visited)
for i in range(k):
    tmp = max(r[i].index(max(r[i])))
    print()

print(visited)
print(hap)
