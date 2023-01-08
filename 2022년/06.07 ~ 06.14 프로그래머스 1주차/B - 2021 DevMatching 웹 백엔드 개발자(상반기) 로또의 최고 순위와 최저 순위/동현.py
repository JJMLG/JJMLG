def solution(lottos, win_nums):
    answer = []
    zero = 0
    tmp = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero += 1
            continue
        
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                tmp += 1     
    
    answer.append(7-(zero+tmp))
    answer.append(7-tmp)
    if answer[0] == 7:
        answer[0] = 6
    if answer[1] == 7:
        answer[1] = 6
  
    return answer