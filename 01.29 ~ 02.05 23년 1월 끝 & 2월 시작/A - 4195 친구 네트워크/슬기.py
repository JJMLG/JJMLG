import sys
sys.stdin = open('input.txt')


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    else:
        parent[y] = x
        visited[x] += visited[y]

def find(z):
    if z != parent[z]:
        parent[z] = find(parent[z])
    return parent[z]

t = int(input())

for _ in range(t):
    f = int(input())
    parent = {}
    visited = {}
    for _ in range(f):
        fr1, fr2 = input().split()

        if fr1 not in parent:
            parent[fr1] = fr1
            visited[fr1] = 1

        if fr2 not in parent:
            parent[fr2] = fr2
            visited[fr2] = 1

        union(fr1, fr2)

        print(visited[find(fr1)])

"""
2
3
3
3

1
7
a b
b c
c a
d e
e d
d e
a b

2
3
3
2
2
2
3
"""