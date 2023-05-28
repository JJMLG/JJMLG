from collections import deque
def solution(s):
    answer = 0
    
    print(list(s))
    queue =deque(list(s))
    for i in range(len(s)):
        stack = []
        flag = False
        for item in queue:
            if item == "[" or item == "{" or item =="(":
                stack.append(item)
                flag = True
            if item == "]" and stack and stack[-1] == "[":
                stack.pop()
            if item == "}" and stack and stack[-1] == "{":
                stack.pop()
            if item == ")" and stack and stack[-1] == "(":
                stack.pop()
        if len(stack) == 0 and flag == True:
            answer += 1
                
        
        
        queue.append(queue.popleft())
    return answer