def solution(new_id):
    answer = ''
    
    # step 1
    new_id = new_id.lower()
    # print(new_id) # 디버깅
    
    # step 2
    for n in new_id:
        if n in 'abcdefghijklmnopqrstuvwxyz1234567890-_.':
            answer = answer + n
    # print(answer) # 디버깅
    
    # step 3
    switch = False
    tmp = ''
    for a in answer:
        if a == '.':
            if not switch:
                switch = True
                tmp = tmp + a
        else:
            tmp = tmp + a
            switch = False
    answer = tmp
    # print(answer) # 디버깅
    
    # step 4
    if len(answer) == 1:
        if answer == '.':
            answer = ''
    else:
        if answer[0] == '.':
            answer = answer[1:]
        elif answer[-1] == '.':
            answer = answer[:len(answer)-1]
    # print(answer) # 디버깅
    
    # step 5
    if answer == '':
        answer = 'a'
    # print(answer) # 디버깅
    
    # step 6
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:len(answer)-1]
    # print(answer) # 디버깅
    
    # step 7
    while len(answer) <= 2:
        answer = answer + answer[-1]
    # print(answer) # 디버깅
    
    return answer