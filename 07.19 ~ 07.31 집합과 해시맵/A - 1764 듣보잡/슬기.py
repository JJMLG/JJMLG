import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
name_1 = set(input() for _ in range(n))
name_2 = set(input() for _ in range(m))
# print(name_1)
# print(name_2)

temp = sorted(list(name_1 & name_2))
print(len(temp))

for i in temp:
    print(i)