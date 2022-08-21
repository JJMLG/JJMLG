import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    arr = input()
    stack = []
    stackidx=0
    for i in range(len(arr)):
        if arr[i]==')':
            if stackidx and stack[stackidx-1] == '(':
                stack.pop(stackidx-1)
                stackidx-=1
            else:
                stack.append(arr[i])
                stackidx+=1
        else:
            stack.append(arr[i])
            stackidx += 1
    if stack:
        print("NO")
    else:
        print("YES")

