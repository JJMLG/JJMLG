def solution(common):
    answer = 0
    c = common
    s = 0 # 0:등차수열 / 1:등비수열
    
    if not (c[1]-c[0] == c[2]-c[1]):
        s = 1
    
    if not s: # 등차
        answer = c[-1] + (c[1]-c[0])
    else: # 등비
        answer = c[-1] * (c[1]//c[0])
    
    return answer