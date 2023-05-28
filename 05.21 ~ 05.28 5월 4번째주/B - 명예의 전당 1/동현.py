from collections import deque

def solution(k, score):
    answer = []
    queue = deque()
    for item in score:
        if len(queue) < k:
            queue.append(item)
            answer.append(min(queue))
        else:
            if item >= min(queue):
                queue.remove(min(queue))
                queue.append(item)
            answer.append(min(queue))
        
    
    return answer