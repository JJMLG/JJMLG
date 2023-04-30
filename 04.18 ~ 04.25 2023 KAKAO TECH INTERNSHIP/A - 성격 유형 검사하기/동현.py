def solution(survey, choices):
    answer = ''
    score = {
        '1' : 3,
        '2' : 2,
        '3' : 1,
        '4' : 0,
        '5' : 1,
        '6' : 2,
        '7' : 3
    }
    dic = {'R': 0,
          'T' : 0,
          'C' : 0,
          'F' : 0,
          'J' : 0,
          'M' : 0,
          'A' : 0,
          'N' : 0,
          }
    
    for i in range(len(survey)):
        if choices[i] > 4:
            dic[survey[i][1]] += score[str(choices[i])]
        else:
            dic[survey[i][0]] += score[str(choices[i])]
    
    tmp = ['RT','CF','JM','AN']
    answer = ""
    for item in tmp:
        if dic[item[0]] > dic[item[1]]:
            answer += dic[item[0]]
        elif dic[item[0]] < dic[item[1]]:
            answer += dic[item[1]]
        else:
            item.sort()
            answer += item[0]
                                
                              
            
                              
                              
            
    return answer