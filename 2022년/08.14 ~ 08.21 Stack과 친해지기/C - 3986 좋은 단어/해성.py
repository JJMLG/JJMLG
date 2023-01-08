import sys
sys.stdin = open('input.txt')
N = int(input())
arr=[]
stack = []
result=0
for i in range(N):
    stack = []
    arr = input()
    stackidx=0
    for j in range(len(arr)):
        if stackidx and arr[j] == stack[stackidx-1]:
            stack.pop(stackidx-1)
            stackidx-=1
        else:
            stack.append(arr[j])
            stackidx += 1
    if (stack):
        continue
    else:
        result+=1
print(result)