import sys
sys.stdin = open('input.txt')

n = int(input())
top = list(input().split())
# top = sorted(list(input().split()))
# print(top)
stack = []
result = [0] * n
top_idx = 0

for i in range(n):
    if not stack:
        stack.append(top[i])
    else:
        if stack[-1] < top[i]:
            stack.append(top[i])
            result[i] = top_idx
            top_idx = i + 1
            # print(top_idx)
        elif stack[-1] >= top[i]:
            result[i] = top_idx
            stack.append(top[i])
            print(stack)
if max(result) == 0:
    print(0)
else:
    print(*result)