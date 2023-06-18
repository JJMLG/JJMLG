def solution(s, skip, index):
    answer = ''
    for item in s:
        cnt = 0
        ordItem = ord(item)
        while cnt < index:
            if ordItem + 1 == 123:
                if 'a' in skip:
                    ordItem = 97
                    continue    
                else:
                    ordItem = 97
                    cnt += 1
                    continue
            if chr(ordItem + 1) in skip:
                ordItem += 1
                continue
            
            ordItem += 1
            cnt += 1
        answer += chr(ordItem)
        # print(ord('a'))
        # print(ord('z'))
    return answer