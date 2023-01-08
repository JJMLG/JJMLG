import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())
set_a = set(list(map(int, input().split())))
set_b = set(list(map(int, input().split())))

gab_a = len(set_a - set_b)
gab_b = len(set_b - set_a)

print(gab_a + gab_b)
