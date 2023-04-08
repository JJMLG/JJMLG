def solution(common):
    c = common
    
    if c[1]-c[0] == c[2]-c[1]: # 등차
        return c[-1] + (c[1]-c[0])
    else: # 등비
        return c[-1] * (c[1]//c[0])