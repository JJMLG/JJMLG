import sys
sys.stdin = open('input.txt')

t = int(input())
for _ in range(t):
    n = int(input())
    for _ in range(n):
        grade, rank = map(int, input().split())
        print(grade, rank)