import sys
sys.stdin=open('input.txt')


n = int(input())
for _ in range(n):
    ls = list(input())
    stack = []
    flag = 0
    for j in range(len(ls)):
        if ls[j] == '(':
            
            stack.append(ls[j])
         
        else:
            if stack == []:
                flag = 1
                break
            if stack[-1] == '(':
                
                stack.pop()
              
    
    if flag or stack:
        print('NO')
    else:
        print('YES')
    
        
