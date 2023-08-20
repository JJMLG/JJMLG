from collections import deque

def solution(storey):
    answer = 0
    
    while storey:
        
        if storey % 10 > 5:
            answer += 10-(storey%10)
            storey += 10
        elif storey % 10 < 5:
            answer += storey % 10
        elif storey % 10 == 5:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += storey % 10
        storey = storey // 10
    return answer
    
    
    
