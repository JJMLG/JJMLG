import sys
sys.stdin = open('input.txt')

n = int(input())
top = list(map(int, input().split()))
# stack = []
# top = []

result = []
cnt = 0
maxx = 0
for i in range(n):
    # stack.append(top[i])
    if maxx <= top[i]:
        maxx = top[i]
        # print(maxx)
        result.append(cnt)
        cnt = 0
    else:
        cnt += 1
result.append(cnt)
# print(result)
print(max(result))