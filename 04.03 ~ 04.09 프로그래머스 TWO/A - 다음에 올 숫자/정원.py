def solution(common):
    c = common
    answer = c[-1]
    
    if c[1]-c[0] == c[2]-c[1]: # 등차
        answer += (c[1]-c[0])
    else: # 등비
        answer *= (c[1]//c[0])
    
    return answer