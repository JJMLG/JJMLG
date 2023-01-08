def solution(dartResult):
    answer = 0
    
    i = 0
    tmp_score = []
    base_score = 0
    while i < len(dartResult):
        if dartResult[i] == '0' and dartResult[i-1].isdigit() == True:
            i += 1
            continue
        
        if dartResult[i].isdigit() == True:
            if dartResult[i+1] == '0':
                base_score = 10
            else:
                base_score = int(dartResult[i])
                
        if dartResult[i] == 'S':
            tmp_score.append(base_score**(1))
            base_score = 0
        if dartResult[i] == 'D':
            tmp_score.append(base_score**(2))
            base_score = 0
        if dartResult[i] == 'T':
            tmp_score.append(base_score**(3))
            base_score = 0
        
        if dartResult[i] == '*':
            if len(tmp_score) >= 2:
                tmp_score[-1] = tmp_score[-1]*2
                tmp_score[-2] = tmp_score[-2]*2
            else:
                tmp_score[-1] = tmp_score[-1]*2
        
        if dartResult[i] == '#':
            tmp_score[-1] = -tmp_score[-1]
                
        i += 1
        print(tmp_score)
    answer=sum(tmp_score)   
    return answer