import sys
sys.stdin = open('input.txt')
N,P = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 1
stack =[]
stackidx=1
stack.append(arr[0])
for i in range(1, N):
    # 프렛같은데 줄 다르면?
    if stackidx and (stack[stackidx-1][1] >= arr[i][1]):
        while(1):
            if stack[stackidx-1][1] > arr[i][1]:
                stack.pop(stackidx-1)
                stackidx -= 1
                result+=1
            elif stack[stackidx-1][1] == arr[i][1]:
                stack.pop(stackidx-1)
                stackidx -= 1
            if not stack:
                break
            result+=1
            stack.append(arr[i])
            stackidx += 1
            break
    else:
        stack.append(arr[i])
        stackidx += 1
        result += 1
print(result)
