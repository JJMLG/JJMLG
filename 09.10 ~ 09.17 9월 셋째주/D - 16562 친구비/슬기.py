import sys
sys.stdin = open('input.txt')

n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
friend = [x for x in range(n+1)]

def find(t):
    if t == friend[t]:
        return t
    friend[t] = find(friend[t])
    return friend[t]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if cost[a] <= cost[b]:
            friend[b] = a
        else:
            friend[a] = b

for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)

ans = 0
for idx, val in enumerate(friend):
    if idx == val:
        ans += cost[idx]

if ans <= k:
    print(ans)
else:
    print("Oh no")