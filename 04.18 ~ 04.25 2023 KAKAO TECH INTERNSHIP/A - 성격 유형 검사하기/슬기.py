def solution(survey, choices):
    score = {'R': 0, 'T': 1, 'C': 2, 'F': 3, 'J': 4, 'M': 5, 'A': 6, 'N': 7}
    typee = [0, 0, 0, 0, 0, 0, 0, 0]

    #   똑같으면 사전 순
    for i in range(len(survey)):
        tmp = choices[i] - 4
        if tmp < 0:
            typee[score[survey[i][0]]] -= tmp
        elif tmp > 0:
            typee[score[survey[i][1]]] += tmp

        # 검사 결과
        # 점수가 같으면 사전순으로 앞서는 문자를 저장해야 한다.
    answer = ''
    if typee[0] < typee[1]:
        answer += 'T'
    else:
        answer += 'R'
    if typee[2] < typee[3]:
        answer += 'F'
    else:
        answer += 'C'
    if typee[4] < typee[5]:
        answer += 'M'
    else:
        answer += 'J'
    if typee[6] < typee[7]:
        answer += 'N'
    else:
        answer += 'A'

    return answer