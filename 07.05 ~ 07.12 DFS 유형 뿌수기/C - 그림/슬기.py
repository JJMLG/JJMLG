import sys
sys.setrecursionlimit(99999)
sys.stdin = open('input.txt')


n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
# print(paper)
# print(n, m)