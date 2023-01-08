import sys
sys.stdin = open('input.txt')
arr = input()
stack = []
stackidx = 0
stack.append(arr[0])
result =0
for i in range(1,len(arr)):
    if arr[i]==')':
        if stack and arr[i-1]=='(':
            stack.pop()
            stack.append('.')
        else:
            stack.append(arr[i])
    else:
        stack.append(arr[i])
stackidx=0
lens=0
pointcnt=0
while('(' in stack):
    lens = len(stack)
    stackidx=0
    garoon=0
    startidx=0
    endidx=0
    for _ in range(lens):
         if stackidx>0 and stack[stackidx]=='.':
             pointcnt += 1
             if stack[stackidx-1]=='(':
                 pointcnt=1
                 startidx=stackidx-1
                 garoon=1
             if (stackidx<lens-1) and (stack[stackidx+1] == ')') and garoon:
                 result += pointcnt+1
                 pointcnt=0
                 stack[stackidx+1]=0
                 stack[startidx]=0
                 garoon=0
         stackidx+=1
    for i in stack:
        if i==0:
            stack.pop(stack.index(i))
    # print(stack)
print(result)