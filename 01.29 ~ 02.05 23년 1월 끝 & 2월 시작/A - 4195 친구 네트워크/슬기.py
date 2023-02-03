import sys
sys.stdin = open('input.txt')

t = int(input())

for _ in range(t):
    f = int(input())
    network = []

    for i in range(1, f+1):
        friend = input().split()
        friend.sort()
        if friend not in network:
            network.append(friend)
    network.sort(key=lambda x: x[0])
    print(network)

    cnt = 0




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