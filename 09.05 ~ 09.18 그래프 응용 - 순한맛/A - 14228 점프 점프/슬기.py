import sys
sys.stdin = open('input.txt')

stone = int(input())
distance = list(map(int, input().split()))
start = int(input())

visited = [0] * stone

cnt = 1
