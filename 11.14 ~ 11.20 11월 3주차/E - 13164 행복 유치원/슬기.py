import sys
sys.stdin = open('input.txt')


n, k = map(int, input().split())
tall = list(map(int, input().split()))

cost = []
for i in range(n-1):
    cost.append(tall[i+1] - tall[i])
cost.sort()
print(sum(cost[:n-k]))


