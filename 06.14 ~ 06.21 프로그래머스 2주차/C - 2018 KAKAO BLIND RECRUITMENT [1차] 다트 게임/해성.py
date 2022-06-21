def solution(dartResult):
    answer = 0
    #     알파벳담에 특수문자나오면 같이
    #  특수문자가 아닌 숫자가 나오면 담꺼
    scores = ['S', 'D', 'T']
    options = ['*', '#']
    temp = dartResult[0]
    result = []
    for i in range(1, len(dartResult)):
        if dartResult[i].isdigit() and dartResult[i - 1] in scores:
            result.append(temp)
            temp = ''
            temp += dartResult[i]
        elif dartResult[i] in options and dartResult[i - 1] in scores:
            temp += dartResult[i]
            result.append(temp)
            temp = ''
        elif i == len(dartResult) - 1:
            temp += dartResult[i]
            result.append(temp)
        else:
            temp += dartResult[i]
    resultTemp = [0 for _ in range(3)]
    resultTemp[0] = result[0]
    temp = ''
    #     네글자도 있음
    for i in range(1, len(result)):
        if len(result[i]) == 3:
            if result[i][2] == '*':
                resultTemp[i - 1] += '*'
                resultTemp[i] = result[i]
            elif result[i][2] == '#':
                resultTemp[i] = result[i]
            else:
                resultTemp[i] = result[i]
        else:
            resultTemp[i] = result[i]
    temp = 0
    starCount = 0
    minusCount = 0
    print(resultTemp)
    for i in range(len(resultTemp)):
        if len(resultTemp[i]) == 2:
            temp += int(resultTemp[i][0]) ** (scores.index(resultTemp[i][1]) + 1)
        #       10s, 1s#
        elif len(resultTemp[i]) >= 3:
            #             두번째가 숫자면 10이니까
            if resultTemp[i][1].isdigit():
                starCount = resultTemp[i][3:].count('*')
                minusCount = resultTemp[i][3:].count('#')
                temp += 10 ** (scores.index(resultTemp[i][2]) + 1) * (2 ** starCount) * ((-1) ** minusCount)
            #         아니면    1s##*
            else:
                starCount = resultTemp[i][2:].count('*')
                minusCount = resultTemp[i][2:].count('#')
                temp += int(resultTemp[i][0]) ** (scores.index(resultTemp[i][1]) + 1) * (2 ** starCount) * (
                            (-1) ** minusCount)

    answer = temp
    return answer
