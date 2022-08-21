import sys

cnt = 0
n = int(input())
for _ in range(n):
    ls = list(input())
    stack = []
    flag = 0
    for j in range(len(ls)):
      
        if stack:
            if stack[-1] == ls[j]:
                stack.pop()
                continue
        stack.append(ls[j])
    
    if stack == []:
        cnt += 1
    

print(cnt)