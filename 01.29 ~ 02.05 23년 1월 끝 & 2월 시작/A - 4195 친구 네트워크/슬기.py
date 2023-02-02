import sys
sys.stdin = open('input.txt')

t = int(input())

for _ in range(t):
    f = int(input())
    network = {}
    cnt = 0
    for _ in range(f):
        fr1, fr2 = input().split()
        if fr1 not in network:
            network[fr1] = 1
        else:
            network[fr1] += 1
            # cnt += 1

        if fr2 not in network:
            network[fr2] = 1
        else:
            network[fr2] += 1
            # cnt += 1

        print(network)
        print(cnt)


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