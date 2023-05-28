def getYaksu(num):
    cnt = 0
    for i in range(1,int(num**(1/2))+1):
        if num % i == 0:
            if i == num//i: 
                cnt += 1
            else:
                cnt += 2
    return cnt

def solution(number, limit, power):
    answer = 0
    
    
    for i in range(1,number+1):
    
        if getYaksu(i) > limit:
            answer += power
        else:
            answer += getYaksu(i)

    
    return answer