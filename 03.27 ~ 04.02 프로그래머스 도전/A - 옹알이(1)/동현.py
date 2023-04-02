def solution(babbling):
    answer = 0
    check = ["aya","ye","woo","ma"]
    for item in babbling:
        tmp = 0
        for c in check:
            if c in item:
                tmp += len(c)
        
        if tmp == len(item):
            answer += 1
    return answer