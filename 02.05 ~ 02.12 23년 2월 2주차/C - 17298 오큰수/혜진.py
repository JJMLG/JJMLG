N = int(input())
arr = list(map(int, input().split()))

stack = []
ans = []

while arr:
    if not stack:
        ans.append(-1)
        stack.append(arr.pop())
    elif stack[-1] > arr[-1]:
        ans.append(stack[-1])
        stack.append(arr.pop())
    else:
        stack.pop()

ans.reverse()
print(*ans)
