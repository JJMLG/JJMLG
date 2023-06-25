def solution(dartResult):
    # 스타상 * > 해당 점수 2배 + 직전 얻은 점수 2배, 4배가 될 수도 있음, -도 2배
    # 아차상 # > 해당 점수 -

    arr = []
    tmp = ''
    for i in range(len(dartResult)):
        if dartResult[i] == '*':
            try:
                arr[-2] = arr[-2] * 2
                arr[-1] = arr[-1] * 2
                tmp = ''
            except:
                arr[-1] = arr[-1] * 2

        elif dartResult[i] == '#':
            arr[-1] = -(arr[-1])
            tmp = ''
        elif dartResult[i] == 'S':

            n = int(tmp)
            arr.append(n)
            tmp = ''
        elif dartResult[i] == 'T':
            n = int(tmp) ** 3
            arr.append(n)
            tmp = ''
        elif dartResult[i] == 'D':
            n = int(tmp) ** 2
            arr.append(n)
            tmp = ''
        else:
            tmp += dartResult[i]

    return sum(arr)