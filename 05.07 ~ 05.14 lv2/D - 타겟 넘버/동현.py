




def solution(numbers, target):
    answer = []
    def dfs(start,tmp):
        
        if start == len(numbers):
            if tmp == target:
                answer.append(1)
            return
        dfs(start+1, tmp + numbers[start])
        dfs(start+1, tmp - numbers[start])
    
    dfs(0,0)
    
    return len(answer)