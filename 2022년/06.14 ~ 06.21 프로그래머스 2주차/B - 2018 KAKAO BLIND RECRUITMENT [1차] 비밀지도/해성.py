def solution(n, arr1, arr2):
    answer = []
    #   N값 2차원 배열 만들고
    # arr1, arr2 2진수로 만들고
    # 두개다 0이면 빈칸, 하나라도 1이면 # 출력
    result1 = []
    result2 = []
    for i in range(n):
        temp1 = ''
        temp2 = ''
        idx1 = bin(arr1[i]).find('b')
        numb1 = bin(arr1[i])[idx1 + 1:]

        idx2 = bin(arr2[i]).find('b')
        numb2 = bin(arr2[i])[idx2 + 1:]

        if len(str(numb1)) < n:
            temp1 += ('0') * (n - len(str(numb1))) + str(numb1)
            result1.append(temp1)
        if len(str(numb1)) >= n:
            result1.append(str(numb1))

        if len(str(numb2)) < n:
            temp2 += ('0') * (n - len(str(numb2))) + str(numb2)
            result2.append(temp2)
        if len(str(numb2)) >= n:
            result2.append(str(numb2))

    for i in range(n):
        tempWord = ''
        for j in range(n):
            if result1[i][j] == '0' and result2[i][j] == '0':
                tempWord += ' '
            else:
                tempWord += '#'
        answer.append(tempWord)
    return answer