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

hap = 0
visited = [0] * (n+10)
print(visited)
for i in range(k):
    for j in range(n):
        if visited[i] != 1:
            if hap < r[i][j]:
                hap += r[i][j]
                visited[i] = 1
                # break
print(visited)
print(hap)
        # if r[i][j]
        # print(r[i][j])
        # print(r[i][j])