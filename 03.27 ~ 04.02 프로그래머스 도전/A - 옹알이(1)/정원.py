def solution(babbling):
    answer = 0
    
    for b in babbling:
        word = ''
        for i in b:
            word += i
            if word in ['aya', 'ye', 'woo', 'ma']:
                word = ''
        if not word:
            answer += 1
            
    return answer