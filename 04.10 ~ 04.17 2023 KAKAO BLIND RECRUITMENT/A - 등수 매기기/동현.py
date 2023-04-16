def solution(score):
    answer = [0]*len(score)
    temp = []
    for i in range(len(score)):
        eng,math = score[i][0],score[i][1]
        temp.append([i,(eng+math)/2])
    
    cnt = 1
    inc = 1
    temp.sort(key=lambda x : -x[1])
    answer[temp[0][0]] = cnt
    for j in range(1,len(temp)):
        if temp[j-1][1] == temp[j][1]:
            answer[temp[j][0]] = cnt
            inc += 1
        else:
            cnt += inc
            answer[temp[j][0]]  = cnt
            inc = 1

    return answer