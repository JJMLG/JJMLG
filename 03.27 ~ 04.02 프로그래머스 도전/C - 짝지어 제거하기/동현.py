def solution(s):
    answer = -1
    
    stack = []
    for i in s:
        
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if stack == []:
        return 1
    else:
        return 0