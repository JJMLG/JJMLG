from collections import deque

def solution(number, k):
    answer = ''
    stack = []
    queue = deque(number)
    stack.append(queue.popleft())
    
    while queue:
        t = queue.popleft()
        while stack and stack[-1] < t and k > 0:
            stack.pop()
            k -=1 
        stack.append(t)
    # print(stack)
    if k == 0:
        return "".join(stack)
    else:
        return "".join(stack[:-k])
  