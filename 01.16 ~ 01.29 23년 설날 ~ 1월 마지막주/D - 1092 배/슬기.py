import sys
sys.stdin = open('input.txt')

n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
m = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)
print(crane, box)


