import sys
sys.stdin = open('input.txt')

m, n = map(int, input().split())
map = [input() for _ in range(m)]
print(map)