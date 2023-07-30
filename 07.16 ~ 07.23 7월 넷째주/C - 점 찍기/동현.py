def solution(k, d):
    answer = 0
    bk = 0
    while bk <= d :
        line = ( d**2 - bk**2 ) ** 0.5
        answer += int(line) // k + 1 
        bk += k
    
    return answer