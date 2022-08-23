import sys
sys.stdin = open('input.txt')

n = int(input())
top = list(map(int, input().split()))

stack = []
result = [] * n

