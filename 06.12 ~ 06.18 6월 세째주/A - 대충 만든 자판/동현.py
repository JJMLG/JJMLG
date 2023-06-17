def solution(keymap, targets):
    answer = []
    dic = {}
    for i in keymap:
        for j in range(len(i)):
            if i[j] not in dic:
                dic[i[j]] =j +1
            else:
                if dic[i[j]] > j +1:
                    dic[i[j]] = j +1
    
    for target in targets:
        temp = 0
        for i in target:
            if i in dic:
                temp += dic[i]
            else:
                temp = -1
                break
        answer.append(temp)
    return answer