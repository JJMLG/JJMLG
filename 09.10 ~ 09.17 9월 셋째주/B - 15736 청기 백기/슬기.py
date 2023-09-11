import sys
sys.stdin = open('input.txt')

n = int(input())
sqrt = []
for i in range(1, int(n**0.5)+1):
    sqrt.append(i)
print(len(sqrt))
