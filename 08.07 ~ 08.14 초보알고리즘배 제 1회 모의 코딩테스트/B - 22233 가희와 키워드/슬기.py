import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
memo = dict()
for _ in range(n):
    memo[input().rstrip()] = 1

res = n
for _ in range(m):
    keyword = sorted(input().rstrip().split(','))
    # print(keyword)
    for i in keyword:
        if i in memo.keys():
            if memo[i] == 1:
                memo[i] -= 1
                res -= 1
    print(res)