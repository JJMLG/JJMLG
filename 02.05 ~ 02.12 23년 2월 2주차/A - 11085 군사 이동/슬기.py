import sys
sys.stdin = open('input.txt')

p, w = map(int, input().split())
c, v = map(int, input().split())

graph = [[] for _ in range(w+1)]
for _ in range(w):
    s, e, l = map(int, input().split())
    # print(s, e, l)
